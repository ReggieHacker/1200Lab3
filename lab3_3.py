#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 22:06:59 2024

@author: reggiehacker
"""

##Example 3
pgrav = {}

#define dictionary with planet names and gravity constant in m/s/s
pgrav["Mercury"] = 3.70
pgrav["Venus"] = 8.87
pgrav["Earth"] = 9.81
pgrav["Mars"] = 3.71
pgrav["Jupiter"] = 24.79
pgrav["Saturn"] = 10.44
pgrav["Neptune"] = 11.15
pgrav["Uranus"] = 8.87

#Prompt user for mass and planet then calculate for weight
mass = float(input('Please enter your mass in kg: '))
p = input('Please enter the planet you want to calculate your weight for: ')
w = mass*pgrav[p]

#print weight on the certain planet
print("You will weigh ", float(w), " N")