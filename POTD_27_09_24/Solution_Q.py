#Sliding window maximum using the Deque(Queue) as the Window n

#User function Template for python3
import heapq
from collections import deque
class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,k,arr):
        
        #code here
        
        q = deque()
        
        nums = arr
        
        for i in range(k-1):
            
            while q and nums[i]>nums[q[-1]]:
                
                q.pop()
                
            q.append(i)
            
        res = []
        
        for i in range(k-1,len(nums)):
            
            if q and q[0]<i-k+1:
                
                q.popleft()
                
            while q and nums[i]>nums[q[-1]]:
                
                q.pop()
                
            q.append(i)
            
            res.append(nums[q[0]])
            
        return res
                
            
        
        


