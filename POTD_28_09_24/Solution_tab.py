#User function Template for python3
class Solution:
    def minimizeCost(self, k, arr):
        # code here
        n=len(arr)
        
        
        dp = [float('inf')]*(n)
        
        dp[0] = 0
        
        for i in range(1,n):
            
            for j in range(1,k+1):
                
                if i-j>=0:
                    
                    jump = dp[i-j] + abs(arr[i]-arr[i-j])
                    
                    dp[i] = min(dp[i],jump)
                    
        return dp[-1]
                    