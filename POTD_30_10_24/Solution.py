#User function Template for python3
from collections import defaultdict
class Solution:
    def countPairsWithDiffK(self,arr, k):
        # code here
        
        map = defaultdict(int)
        
        count = 0
        
        
        for i,x in enumerate(arr):
            
            if x-k in map:
                
                count+=map[x-k]
                
            if x+k in map:
                
                count+=map[x+k]
                
            map[x]+=1
            
        return count

