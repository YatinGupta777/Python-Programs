#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 18:47:08 2018

@author: yatingupta
"""

# Python code to segregate even odd 
# numbers in an array 
# Function to segregate even odd numbers 
def arrayEvenAndOdd(arr,n):
    i = -1
    j= 0 
    while (j!=n):
        if (arr[j] % 2 ==0):
            i = i+1
            # Swapping even and odd numbers 
            arr[i],arr[j] = arr[j],arr[i]
            
        j = j+1
    
    # Printing segregated array 
    for i in arr:
        print (str(i) + " " ,end='')
        
# Driver Code
arr = [1, 3, 2, 4, 7, 6, 9, 10 ]
n = len(arr)
arrayEvenAndOdd(arr,n)

# This code was contributed by Yatin Gupta