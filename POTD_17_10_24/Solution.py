#User function Template for python3
'''
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def alternatingSplitList(self, head):
        #Your code here
        
        pointer1  = head
        
        pointer2 = head.next
        
        odd_start = head 
        
        even_start = head.next
        
        
        while pointer2 and pointer2.next:
            
            pointer1.next = pointer1.next.next
            
            pointer2.next = pointer2.next.next
            
            pointer1 = pointer1.next
            
            pointer2 = pointer2.next
            
        pointer1.next = None
        
        return odd_start , even_start