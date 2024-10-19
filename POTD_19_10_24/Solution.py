#User function Template for python3

class Solution:
    def roundToNearest (self, str) : 
        #Complete the function
        
        N=int(str)
        one=N//10
        one= one*10    #nearest lower bound
        two = one+10  #nearest upper bound 
        if (abs(one-N) <= abs(two-N)):
            return one
        else:
            return two
