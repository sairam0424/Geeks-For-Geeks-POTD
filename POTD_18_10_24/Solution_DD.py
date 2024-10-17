#User function Template for python3
from collections import defaultdict , Counter
class Solution:
    
    def getSingle(self,arr):
        # code here
        
        map = defaultdict(int)
        
        for ele in arr:
            
            map[ele]+=1
            
        for key,freq in map.items():
            
            if freq&1 == 1:
                
                return key
                
                
                
        
                
        