class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        # Code here
        
        n = len(arr)
        
        maxa = 0
        
        for i in range(n):
            
            for j in range(n):
                
                if arr[i] == arr[j]:
                    
                    maxa = max(maxa,j-i)
                    
        
        return maxa

