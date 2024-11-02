#User function Template for python3
class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        # your code
        
        n = len(arr)
        
        seen = set()
        
        for i in range(n):
            
            if arr[i] in seen:
                
                return True
                
            else:
                
                seen.add(arr[i])
                
            if i>=k:
                
                seen.remove(arr[i-k])
                
        return False

