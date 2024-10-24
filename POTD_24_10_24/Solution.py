#User function Template for python3

class Solution:
    def modifyAndRearrangeArr (self, arr) : 
        #Complete the function
        
        for i in range(len(arr)-1):
            
            if arr[i] == arr[i+1]:
                
                arr[i] = arr[i]*2
        
                arr[i+1] = 0
                
        start = 0 
        
        for i in range(len(arr)):
            
            
            if arr[i]!=0:
                
                arr[i],arr[start] = arr[start],arr[i]
                
                start+=1
                
        return arr