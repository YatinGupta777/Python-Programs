# Python program to find maximum product subarray 
import sys
  
# Function for maximum product 
def max_product(arr, n):
 
    # Initialize maximum products in forward and 
    # backward directions 
    max_fwd = -sys.maxsize -1
    max_bkd = -sys.maxsize -1 
  
    # Initialize current product 
    max_till_now = 1 
  
    # max_fwd for maximum contiguous product in 
    # forward direction 
    # max_bkd for maximum contiguous product in 
    # backward direction 
    # iterating within forward direction in array 
    for i in range(n): 
     
        # if arr[i]==0, it is breaking condition 
        # for contiguos subarray 
        max_till_now = max_till_now * arr[i]
        if (max_till_now == 0):
             max_till_now = 1; 
             continue
         
        if (max_fwd < max_till_now):   #update max_fwd 
            max_fwd = max_till_now 
     
  
    max_till_now = 1 
  
    # iterating within backward direction in array 
    for i in range(n-1,-1,-1):
        max_till_now = max_till_now * arr[i] 
        
        if (max_till_now == 0): 
            max_till_now = 1
            continue  
  
        # update max_bkd 
        if (max_bkd < max_till_now) : 
            max_bkd = max_till_now 
  
    # return max of max_fwd and max_bkd 
    res =  max(max_fwd, max_bkd) 
  
    # Product should not be nagative. 
    # (Product of an empty subarray is 
    # considered as 0) 
    return max(res, 0) 

  
# Driver Program to test above function 
 
arr = [-1, -2, -3, 4] 
n = len(arr) 
print(max_product(arr, n))

 