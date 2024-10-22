#User function Template for python3
from collections import defaultdict
class Solution:
    def sameOccurrence(self, arr, x, y):
        # code here
        
        map = defaultdict(int)
        
        map[0] = 1
        
        countX = 0
        
        countY = 0
        
        res = 0
        
        for i in range(len(arr)):
            
            if arr[i] == x:
                
                countX+=1
                
            if arr[i] == y:
                
                countY+=1
                
            difference = countX - countY
            
            res += map[difference]
            
            map[difference]+=1
            
        return res
