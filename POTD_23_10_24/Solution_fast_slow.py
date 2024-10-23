
'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def sumOfLastN_Nodes(self, head, n):
        #function should return sum of last n nodes
        
        fast = slow = head
        
        while n:
            
            fast = fast.next
            
            n-=1
            
        while fast:
            
            fast = fast.next
            
            slow = slow.next
            
        sum = 0
        
        while slow:
            
            sum+=slow.data
            
            slow = slow.next
            
        return sum