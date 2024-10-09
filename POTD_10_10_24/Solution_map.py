class Solution:
    # Your task is to Complete this function
    # function should return an integer
    def maxDistance(self, arr):
        # Code here
        
        map = {}
        
        maxa = 0
        
        n = len(arr)
        
        for i in range(n):
            
            if arr[i] not in map:
                
                map[arr[i]] = i
                
            else:
                
                maxa = max(maxa,i-map[arr[i]])
                
        return maxa
