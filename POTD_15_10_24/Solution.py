#User function Template for python3

class Solution:
    
    #Complete this fuction
    #Function to count the number of subarrays which adds to the given sum.
    def subArraySum(self,arr, tar):
        #Your code here
        
        
        count  = 0
        
        
        n = len(arr)
        
        
        for i in range(n):
            
            cur_sum  = 0
            
            for j in range(i,n):
                
                cur_sum+=arr[j]
                
                if cur_sum == tar :
                    
                    count+=1
                    
        return count
                
                
        
        