class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        
        arr.sort(reverse = True)
        
        ans = []
        
        pointer1 = 0
        
        pointer2 = len(arr)-1
        
        while pointer1<=pointer2:
            
            ans.append(arr[pointer1])
            
            if pointer1 == pointer2:
                
                
                break
            
            ans.append(arr[pointer2])
            
            
            
            pointer1+=1
            
            pointer2-=1
            
        return ans