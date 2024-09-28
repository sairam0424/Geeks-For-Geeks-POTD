#User function Template for python3
class Solution:
    def minimizeCost(self, k, arr):
        # code here
        
        n=len(arr)
        
        # memo = {}
        
        dp = [-1]*(n)
        
        def dfs(arr,n,k):
            
            if n==0:
                
                return 0
                
            mini = float('inf')
            
            # if n in memo:
                
            #     return memo[n]
            
            if dp[n]!=-1:
                
                return dp[n]
            
            for i in range(1,k+1):
                
                if n-i>=0:
                    
                    jump = dfs(arr,n-i,k) + abs(arr[n]-arr[n-i])
                    
                    mini = min(mini,jump)
                    
            dp[n] = mini
            
            return dp[n]
                    
            # memo[n] = mini
            
            # return memo[n]
        
        return dfs(arr,n-1,k)
        