#User function Template for python3

class Solution:
    def maxSum(self,arr):
        # code here
        
        arr.sort()
        
        res = 0
        
        n=len(arr)
        
        for i in range(n):
            
            res+=abs(arr[i]-arr[n-i-1])
            
        return res
