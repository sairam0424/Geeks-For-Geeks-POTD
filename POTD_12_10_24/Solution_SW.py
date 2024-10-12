class Solution:
    def pairWithMaxSum(self, arr):
        #code here
        
        if len(arr) == 1:
            
            return -1
            
        maxa = arr[0] + arr[1]
        
        cur_sum = maxa
        
        left = 0
        
        for right in range(2,len(arr)):
            
            cur_sum+=arr[right]
            
            cur_sum-=arr[left]
            
            left+=1
            
            if cur_sum>maxa:
                
                maxa = cur_sum
                
        return maxa
            