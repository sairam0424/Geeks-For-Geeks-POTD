
# from typing import List


class Solution:
    def rotateDelete(self,  arr):
        # code here
        k = 1
        while len(arr) > 1:
            # Rotate
            arr.insert(0, arr.pop(-1))
            
            # Remove kth element
            arr.pop(-k)
            k += 1
            
            if k > len(arr):
                break
                
        return arr[0]