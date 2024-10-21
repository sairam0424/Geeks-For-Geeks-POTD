#User function Template for python3
class Solution:
    def countgroup(self,arr): 
        #Complete the function
        
        xor = 0
        
        for num in arr:
            
            xor^=num
            
        if xor == 0:
            
            return 2**(len(arr)-1)-1
            
        else:
            
            return 0

