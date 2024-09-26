#User function Template for python3

class Solution:
    
    #Function to find maximum number of consecutive steps 
    #to gain an increase in altitude with each step.
    def maxStep(self, arr):
        #Your code here
        
        count = 0
        
        maxa = float('-inf')
        
        for i in range(1,len(arr)):
            
            if arr[i]>arr[i-1]:
                
                count+=1
                
            else:
                
                maxa = max(maxa,count)
                
                
                count = 0
                
                
        return max(maxa,count)