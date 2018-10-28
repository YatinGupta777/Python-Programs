 
# Python program to find type of array, ascending 
# descending, clockwise rotated or anti-clockwise 
# rotated. 
def findType(arr, n) :
 
    i = 0; 
  
    # Check if the array is in ascending order 
    while (i < n-1 and arr[i] <= arr[i+1]) :
        i=i+1
  
    # If i reaches to last index that means 
    # all elements are in increasing order 
    if (i == n-1):
        print("Ascending with maximum element = " + str(arr[n-1]))
        return None
     
  
    # If first element is greater than next one 
    if (i == 0):
        while (i < n-1 and arr[i] >= arr[i+1]):
            i=i+1; 
  
        # If i reaches to last index 
        if (i == n - 1):
            print( "Descending with maximum element =  " + str(arr[0]))
            return None 
    
  
        # If the whole array is not in decreasing order 
        # that means it is first decreasing then 
        # increasing, i.e., descending rotated, so 
        # its maximum element will be the point breaking 
        # the order i.e. i so, max will be i+1 
        if (arr[0] < arr[i+1]):
            print( "Descending rotated with maximum element = " + str(max(arr[0], arr[i+1])))
            return  None
        else:
         
            print("Ascending rotated with maximum element = " + str(max(arr[0], arr[i+1]))) 
            return None
         
     
  
    # If whole array is not increasing that means at some 
    # point it is decreasing, which makes it ascending rotated 
    # with max element as the decreasing point 
    if (i < n -1 and arr[0] > arr[i+1]):
     
        print( "Ascending rotated with maximum element =  " + str(max(arr[i], arr[0])))
        return None
     
  
    print( "Descending rotated with maximum element " + str(max(arr[i],arr[0])))

# Driver code 

arr1 = [ 4, 5, 6, 1, 2, 3] # Ascending rotated 
n = len(arr1)
findType(arr1, n); 
  
arr2 = [ 2, 1, 7, 5, 4, 3] # Descending rotated 
n = len(arr2) 
findType(arr2, n); 
  
arr3 = [ 1, 2, 3, 4, 5, 8] # Ascending 
n = len(arr3) 
findType(arr3, n); 
  
arr4 = [ 9, 5, 4, 3, 2, 1] # Descending 
n = len(arr4) 
findType(arr4, n); 
  

 