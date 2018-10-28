#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 20:06:54 2018

@author: yatingupta
"""

def printfrequency(arr,n):
    
    # Subtract 1 from every element so that the elements
    # become in range from 0 to n-1
    for j in range(0,n):
        arr[j] = arr[j]-1
    
    # Use every element arr[i] as index and add 'n' to 
    # element present at arr[i]%n to keep track of count of 
    # occurrences of arr[i] 
    for i in range(0,n):
        arr[arr[i]%n] = arr[arr[i]%n] + n
     
    # To print counts, simply print the number of times n 
    # was added at index corresponding to every element
    
    for i in range(0,n):
        print (str(i+1) + " -> " + str(int(arr[i]/n)))
        
# Driver program to test above function 
arr = [2, 3, 3, 2, 5] 
printfrequency(arr, len(arr))

# This code is contributed by Yatin Gupta
        
    