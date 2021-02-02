#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 12:57:45 2021

@author: lkst
"""
import numpy as np
import scipy.special as sp

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
    
input_nodes = 3
hidden_nodes = 3
output_nodes = 3
learning_rate = 0.3

n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
print(n.query([1.0, 0.5, -1.5]))














