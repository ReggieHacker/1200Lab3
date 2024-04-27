#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 22:06:58 2024

@author: reggiehacker
"""

##Example 1
import numpy as np

#grab user input for the x component of vector
print('What is the x component of your vector: ')
x = float(input())

#grab user input for the y component of vector
print('What is the y component of your vector: ')
y = float(input())

#create list for the vector components
comp = (x, y)

#calculate magnitude of vector
mag = np.sqrt(x**2 + y**2)

#print outputs
print("The componenents of the vector are " + comp)
print("The magnitude of the vector is " + mag)