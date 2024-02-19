#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 14:43:34 2024

@author: reggiehacker
"""

# =============================================================================
# ##Example 1
# import numpy as np
# 
# print('What is the x component of your vector: ')
# x = float(input())
# 
# print('What is the y component of your vector: ')
# y = float(input())
# 
# comp = (x, y)
# 
# mag = np.sqrt(x**2 + y**2)
# 
# print("The componenents of the vector are " + comp)
# print("The magnitude of the vector is " + mag)
# =============================================================================


# =============================================================================
# ##Example 2
# plist = [1, 2, 3, 5, 7]
# print(plist)
# 
# #Add a few more primes to list
# plist.extend([11, 13, 17])
# print(plist)
# 
# #Access first and last prime numbers from list
# print(plist[0], plist[-1])
# 
# #Create list only containing first three primes
# nplist = plist[:3]
# print(nplist)
# 
# #Combine the original list with another list of primes
# nplist2 = [19, 23, 29]
# plist.extend(nplist2)
# print(plist)
# 
# #reverse list
# plist.reverse()
# print(plist)
# =============================================================================


# =============================================================================
# ##Example 3
# pgrav = {}
# 
# #define dictionary
# pgrav["Mercury"] = 3.70
# pgrav["Venus"] = 8.87
# pgrav["Earth"] = 9.81
# pgrav["Mars"] = 3.71
# pgrav["Jupiter"] = 24.79
# pgrav["Saturn"] = 10.44
# pgrav["Neptune"] = 11.15
# pgrav["Uranus"] = 8.87
# 
# #Prompt user for mass and planet then calculate for weight
# mass = float(input('Please enter your mass in kg: '))
# p = input('Please enter the planet you want to calculate your weight for: ')
# w = mass*pgrav[p]
# 
# print("You will weigh ", float(w), " N")
# =============================================================================
