#User function Template for python3

class Solution:
    def totalCount(self, k, arr):
        # code here
        
        count = 0
        
        for element in arr:
            
            count += element//k
            
            if element%k:
                
                count+=1
                
        return count
                
            