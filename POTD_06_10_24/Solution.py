#User function Template for python3

import sys
sys.setrecursionlimit(10**8)
class Solution:
    def numIslands(self,grid):
        #code here
        def dfs(grid,s,d,di,dj):
            if s<0 or d<0 or s>=len(grid) or d>=len(grid[0]) or grid[s][d]!=1:
                return 
            grid[s][d]=0
            for i in range(8):
                dfs(grid,s+di[i],d+dj[i],di,dj)
                
                
        n=len(grid[0])
        m=len(grid)
        c=0
        di=[-1,1,0,0,-1,-1,1,1]
        dj=[0,0,-1,1,-1,1,-1,1]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    dfs(grid,i,j,di,dj)
                    c+=1
        return c
        



