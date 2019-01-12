
#Function to compute widest gap
def widestGap( n, start, finish):
    
    start_index = 1
    finish_index = 0
    diff = 0
    max_diff = 0
    
    start.sort()
    finish.sort()

    #Checking for the length between first car and start of road
    max_diff = max(max_diff, start[0]-1)

    while(start_index < len(start)):
    
          if(start[start_index] > finish[finish_index]):
                 diff = abs(start[start_index] - finish[finish_index] - 1 )
          max_diff = max(max_diff, diff)
          start_index = start_index +1
          finish_index = finish_index + 1
    
    #Checking for the length between end of road and finish of last car
    max_diff = max(max_diff, n-finish[len(finish)-1])
    return max_diff


#Driver Code

n = 10
start = [1,2,5,8]
finish = [2,2,6,10]
print("Widest Gap Between cars : " + str(widestGap(n, start, finish)))


   