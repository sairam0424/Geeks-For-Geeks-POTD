#User function Template for python3

class Solution:
    def findSmallest(self, arr):
        # code here
        
        not_a_number  = 1
        
        for num in arr:
            
            if num>not_a_number:
                
                return not_a_number
                
            not_a_number+=num
            
        return not_a_number
