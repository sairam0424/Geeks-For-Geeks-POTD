
from collections import defaultdict
class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        # your code
        
        map = defaultdict(int)
        
        for i,x in enumerate(arr):
            
            if x in map:
                
                if i-map[x]<=k:
                    
                    return True
                    
            map[x] = i
            
        return False