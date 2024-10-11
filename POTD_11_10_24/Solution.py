class Solution:
    def rearrange(self, arr):
        #Code here
        
        n = len(arr)
        
        new_arr = [-1]*(n)
        
        arr = set(arr)
        
        for i in range(n):
            
            if i in arr:
                
                new_arr[i] = i 
                
        return new_arr
        