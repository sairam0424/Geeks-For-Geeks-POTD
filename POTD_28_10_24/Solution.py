
from collections import defaultdict
class Solution:
   
    def removeDuplicates(self, arr):
        # code here 
        map = defaultdict(int)
       
        for ele in arr:
           
           map[ele]+=1
           
        return map.keys()