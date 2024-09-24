
from collections import Counter,defaultdict

class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, t):
        map=defaultdict(int)

        for i in t:

            map[i]+=1

        left=0

        right=0

        start_index=-1

        end_index=-1

        min_len=float('inf')

        seen_count=0

        for right in range(len(s)):

            if map[s[right]]>0:

                seen_count+=1

            map[s[right]]-=1

            while seen_count==len(t):

                if right-left+1<min_len:

                    min_len=right-left+1

                    start_index=left

                    end_index=right 

                map[s[left]]+=1

                if map[s[left]]>0:

                    seen_count-=1

                left+=1

        if start_index==-1:

            return -1

        else:

            return s[start_index:end_index+1]       

                
        
        

