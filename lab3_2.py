#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 22:06:59 2024

@author: reggiehacker
"""

##Example 2
plist = [1, 2, 3, 5, 7]
print(plist)

#Add a few more primes to list
plist.extend([11, 13, 17])
print(plist)

#Access first and last prime numbers from list
print(plist[0], plist[-1])

#Create list only containing first three primes
nplist = plist[:3]
print(nplist)

#Combine the original list with another list of primes
nplist2 = [19, 23, 29]
plist.extend(nplist2)
print(plist)

#reverse list
plist.reverse()
print(plist)