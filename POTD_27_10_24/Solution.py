class Solution:
    def findTriplet(self, arr):
        
        vis = set(arr)
        
        for i in range(len(arr)):
            
            for j in range(i+1,len(arr)):
                
                cur_sum = arr[i]+arr[j]
                
                if cur_sum in vis:
                    
                    return True
                    
        return False