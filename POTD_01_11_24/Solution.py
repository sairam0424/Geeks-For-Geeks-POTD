#User function Template for python3

class Solution:
    def maxSum(self,arr):
        # code here
        
        arr.sort()
        
        n=len(arr)
        
        i =0
        
        j=n-1
        
        ans = 0
        
        while i<j:
            
            ans+=abs(arr[i]-arr[j])
            
            i+=1
            
            j-=1
            
        return 2*ans
            
            
        
