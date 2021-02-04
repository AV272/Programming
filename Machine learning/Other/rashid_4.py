#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 12:37:29 2021

@author: lkst
"""

import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt
import imageio
import glob # helps work with filepath

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
    
    
    ## TESTING OF NEURAL NETWORK ON MY OWN NUMBERS
    
    our_own_dataset = []

    # ? -- one symbol
    for image_file_name in glob.glob('/home/lkst/github/Programming/Machine learning/Other/Data/?.png'):
        print('loading ...', image_file_name)
        # take true answer from file name
        label = int(image_file_name[-5:-4])
        # load image from png into array
        img_array = imageio.imread(image_file_name, as_gray=True)
        # reshape 28x28 into 784 array
        img_data = 255.0 - img_array.reshape(784)
        img_data = (img_data/255.0*0.99) + 0.01
        print(np.min(img_data))
        print(np.max(img_data))
        # create list from label and image data
        record = np.append(label, img_data)
        our_own_dataset.append(record)
        pass
    
    
    for item in range(5):
        
        plt.imshow(our_own_dataset[item][1:].reshape(28,28), cmap='Greys',interpolation='None')
        correct_label = our_own_dataset[item][0]
        inputs = our_own_dataset[item][1:]
        
        outputs = n.query(inputs)
        print(outputs)
        
        label = np.argmax(outputs)
        print('Network answer ', label)
        print('Correct answer ', correct_label)
        if (label == correct_label):
            print("Match")
        else:
            print('No match')
            pass
        pass
    pass



