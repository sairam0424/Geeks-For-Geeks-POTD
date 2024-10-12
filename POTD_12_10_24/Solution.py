class Solution:
    def pairWithMaxSum(self, arr):
        #code here
        
        if len(arr) == 1:
            
            return -1
            
        maxa = float('-inf')
        
        for i in range(len(arr)-1):
            
            maxa = max(maxa,arr[i]+arr[i+1])
            
        return maxa