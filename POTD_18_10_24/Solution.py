#User function Template for python3

#Brute force -> tle at test case 10 -> 10/116
from collections import defaultdict , Counter
class Solution:
    
    def getSingle(self,arr):
        # code here
        
        for ele in arr:
            
            count = arr.count(ele)
            
            if count%2==1:
                
                return ele
                
        
                
        