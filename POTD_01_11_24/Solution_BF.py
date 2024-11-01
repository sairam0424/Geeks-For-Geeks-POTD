#User function Template for python3

class Solution:
    def maxSum(self,arr):
        # code here
        
        arr.sort()
        
        re_arr = []
        
        pointer1 = 0
        
        pointer2 = len(arr)-1
        
        while pointer1<pointer2:
            
            
            re_arr.append(arr[pointer1])
            
            re_arr.append(arr[pointer2])
            
            pointer2-=1
            
            pointer1+=1
            
        maxa = abs(re_arr[-1] - re_arr[0])
        
        # print(re_arr)
        
        # print(maxa)
        
        for i in range(1,len(re_arr)):
            
            maxa+=abs(re_arr[i-1]-re_arr[i])
            
        return maxa
            
            
        
        
        
      
            
            
            