class Solution:
    # Function to find the:majority elements in the array
    def findMajority(self, nums):
        #Your Code goes here.
        
        n = len(nums)
        
        if n==0:
            
            return [-1]
            
        cand1 = 0
        
        cand2 = 0
        
        count1 = 0 
        
        count2  = 0
        
        for num in nums:
            
            if num == cand1:
                
                count1+=1
            
            elif num == cand2:
                
                count2+=1
                
            elif count1==0:
                
                cand1 = num
                
                count1 = 1
                
            elif count2==0:
                
                cand2=num
                
                count2=1
                
            else:
                
                count1-=1
                
                count2-=1
                
        count1=0
        
        count2=0
        
        for num in nums:
            
            if num == cand1:
                
                count1+=1
                
            elif num == cand2:
                
                count2+=1
                
        res = []
        
        if count1>n//3:
            
            res.append(cand1)
            
        if count2>n//3:
            
            res.append(cand2)
        
        if len(res) == 0:
            
            return [-1]
            
        else:
            
            return res
            