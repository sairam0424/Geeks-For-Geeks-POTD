
from typing import List


class Solution:
    def pairsum(self, arr : List[int]) -> int:
        # code here
        
        n = len(arr)
        
        maxa_sum = float('-inf')
        
        left = 0
        
        right = n-1
        
        while left<right:
            
            if arr[left] + arr[right] > maxa_sum:
                
                maxa_sum = arr[left] + arr[right]
                
            elif arr[left] < arr[right]:
                
                left+=1
                
            else:
                
                right-=1
                
        return maxa_sum