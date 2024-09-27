#Heap Solution (MAX Heap)

#User function Template for python3
import heapq
class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,k,arr):
        
        #code here
        n=len(arr)
        h=[]
        r=[]
        for i in range(k):
            heapq.heappush(h,(-arr[i],i))
        r.append(-h[0][0])
        for i in range(n-k):
            while h and h[0][1]<=i:
                heapq.heappop(h)
            heapq.heappush(h,(-arr[i+k],i+k))
            r.append(-h[0][0])
        return r
        



