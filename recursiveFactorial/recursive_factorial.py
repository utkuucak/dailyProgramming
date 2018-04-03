# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 21:34:07 2018

@author: Toshiba
"""

def factorial(x):
    if x < 0:
        print("X must be a non-negative number!")
        return -1
    if x == 0:
        return 1
    if x > 0:
       return x * factorial(x-1)
    
    
print(factorial(5))    
        