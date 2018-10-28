
#https://www.geeksforgeeks.org/find-the-missing-number/


# getMissingNo takes list as argument 
def getMissingNo(A):
    n = len(A)
    x1 = A[0]
    x2 = 1
    for i in range(1,n):
        x1 = x1 ^ A[i]
    for i in range(2,n+2):
        x2 = x2^i
    
    return x1 ^ x2


# Driver program to test above function 
A = [1, 2, 4, 5, 6] 
miss = getMissingNo(A) 
print(miss) 
# This code is contributed by Yatin Gupta   
    

    