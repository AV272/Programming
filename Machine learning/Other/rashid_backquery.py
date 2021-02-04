#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:00:19 2021

@author: lkst
"""

import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

# definition of neural network class 
class neuralNetwork:
    
    # initialization function
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        
        # put a number of nodes in leyers
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        
        # learning coeffition
        self.lr = learningrate
        
        # matrix of weight coefficients
        #self.w_ih = np.random.rand(self.hnodes, self.inodes) - 0.5
        #self.w_ho = np.random.rand(self.onodes, self.hnodes) - 0.5
        
        # coefficient from normal distribution
        self.w_ih = np.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.w_ho = np.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))
        
        # sigmoid function
        self.activation_function = lambda x: sp.expit(x)
        self.inverse_activation_function = lambda x: sp.logit(x)

        pass
    
    # training of neural network
    def train(self, inputs_list, targets_list):
        
        # translate data to 2D-array
        inputs = np.array(inputs_list, ndmin=2).T
        targets = np.array(targets_list, ndmin=2).T # answers
                
        # get signals for hidden layer
        hidden_inputs = np.dot(self.w_ih, inputs)
        # using sigmoid function on hidden inputs
        hidden_outputs = self.activation_function(hidden_inputs)
        
        # get signals for output layer
        final_inputs = np.dot(self.w_ho, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        
        # computation of errors
        output_errors = targets - final_outputs
        hidden_errors = np.dot(self.w_ho.T, output_errors)
        
        # rewriting of weights coefficients
        self.w_ho += self.lr*np.dot((output_errors*final_outputs*(1- final_outputs)),\
                                    np.transpose(hidden_outputs))
        self.w_ih += self.lr*np.dot((hidden_errors*hidden_outputs*(1- hidden_outputs)),\
                                    np.transpose(inputs))
        
        pass
    
    # going by network
    def query(self, inputs_list):
        # translate data to 2D-array
        inputs = np.array(inputs_list, ndmin=2).T
        
        # get signals for hidden layer
        hidden_inputs = np.dot(self.w_ih, inputs)
        # using sigmoid function on hidden inputs
        hidden_outputs = self.activation_function(hidden_inputs)
        
        # get signals for output layer
        final_inputs = np.dot(self.w_ho, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        
        return(final_outputs)
    
    # backquery the neural network
    # we'll use the same termnimology to each item, 
    # eg target are the values at the right of the network, albeit used as input
    # eg hidden_output is the signal to the right of the middle nodes
    def backquery(self, targets_list):
        # transpose the targets list to a vertical array
        final_outputs = np.array(targets_list, ndmin=2).T
        
        # calculate the signal into the final output layer
        final_inputs = self.inverse_activation_function(final_outputs)

        # calculate the signal out of the hidden layer
        hidden_outputs = np.dot(self.w_ho.T, final_inputs)
        # scale them back to 0.01 to .99
        hidden_outputs -= np.min(hidden_outputs)
        hidden_outputs /= np.max(hidden_outputs)
        hidden_outputs *= 0.98
        hidden_outputs += 0.01
        
        # calculate the signal into the hidden layer
        hidden_inputs = self.inverse_activation_function(hidden_outputs)
        
        # calculate the signal out of the input layer
        inputs = np.dot(self.w_ih.T, hidden_inputs)
        # scale them back to 0.01 to .99
        inputs -= np.min(inputs)
        inputs /= np.max(inputs)
        inputs *= 0.98
        inputs += 0.01
        
        return inputs

# number of input, hidden, output nodes
input_nodes = 784
hidden_nodes = 150
output_nodes = 10
learning_rate = 0.2

lr_arr = []
eff_arr = []

for num in range(1):
    
    #hidden_nodes = num*50 + 50
    n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
    
    # getting data for training
    training_data_file = open('/home/lkst/github/Programming/Machine learning/Other/Data/mnist_train.csv', 'r')
    training_data_list = training_data_file.readlines()
    training_data_file.close()
    
    ## TRAINING OF NEURAL NETWORK
    # using few epochs
    epochs = 6
    for e in range(epochs):
        
        for record in training_data_list:
            all_values = record.split(',')
            inputs = (np.asfarray(all_values[1:])/255.0*0.99) + 0.01 # rewrite values to interval [0.01, 1]
            
            # take the answers
            targets = np.zeros(output_nodes) + 0.01
            targets[int(all_values[0])] = 0.99
            n.train(inputs, targets)
            pass
        pass
    
    
    # getting data for testing
    test_data_file = open('/home/lkst/github/Programming/Machine learning/Other/Data/mnist_test.csv', 'r')
    test_data_list = test_data_file.readlines()
    test_data_file.close()
    
    ## TESTING OF NEURAL NETWORK
    
    # journal of net work
    scorecard = []
    
    for record in test_data_list:
        all_values = record.split(',')
        
        correct_lable = int(all_values[0]) # right answer
        #print(correct_lable, 'true marker')
        
        inputs = (np.asfarray(all_values[1:])/255.0*0.99) + 0.01 # rewrite values to interval [0.01, 1]
        outputs = n.query(inputs) # going by the network with taken coefficients
        label = np.argmax(outputs) # take maximal value in outputs
        #print(label, 'answer of network')
        
        if (label == correct_lable):
            scorecard.append(1)
        else:
            scorecard.append(0)
            pass
        pass
    
    #print(scorecard)
    
    # compute effectiveness of the network
    scorecard_array = np.asarray(scorecard)
    print('Effectiveness = ', scorecard_array.sum()/scorecard_array.size)
    eff = scorecard_array.sum()/scorecard_array.size
    lr_arr.append(epochs)
    eff_arr.append(eff)
    
    # run the network backwards, given a label, see what image it produces
    
    fig, axs = plt.subplots(1, 10)
    for lb in range(10):
        # label to test
        label = lb
        # create the output signals for this label
        targets = np.zeros(output_nodes) + 0.01
        # all_values[0] is the target label for this record
        targets[label] = 0.99
        print(targets)
        
        # get image data
        image_data = n.backquery(targets)
        
        # plot image data
        
        
        axs[lb].imshow(image_data.reshape(28,28), cmap='Greys', interpolation='None')
    pass

# создаём рисунок с координатную плоскость
#fig = plt.subplots()
# создаём область, в которой будет отображаться график
# значения x, которые будут отображены
# количество элементов в созданном массиве - качество прорисовки графика 
# рисуем график
#plt.plot(lr_arr, eff_arr,'ro')
# показываем график
plt.show() 













