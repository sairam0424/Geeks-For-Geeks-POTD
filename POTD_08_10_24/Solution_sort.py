
from typing import List


class Solution:
    def pairsum(self, arr : List[int]) -> int:
        # code here
        
        arr.sort()
        
        return arr[-1] + arr[-2]
        

