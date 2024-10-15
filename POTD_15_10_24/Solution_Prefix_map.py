#User function Template for python3
from collections import defaultdict
class Solution:
    
    #Complete this fuction
    #Function to count the number of subarrays which adds to the given sum.
    def subArraySum(self,arr, tar):
        #Your code here
        
        map = defaultdict(int)

        map[0] = 1
        
        prefix_sum = 0
        
        count = 0
        
        for num in arr:  
            
            prefix_sum += num
            
            required_value = prefix_sum - tar
            
            if required_value in map:
                
                count+=map[required_value]
                
            map[prefix_sum]+=1
            
            
        return count
            
            