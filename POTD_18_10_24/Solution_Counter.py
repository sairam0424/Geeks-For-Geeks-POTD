#User function Template for python3
from collections import defaultdict , Counter
class Solution:
    
    def getSingle(self,arr):
        # code here
        
        c=Counter(arr)
        
        for key,feq in c.items(): 
            
            if feq&1 == 1:
                
                return key
                
        