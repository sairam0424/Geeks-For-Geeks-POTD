#User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
'''
class Solution:
    #Function to insert a node in a sorted doubly linked list.
    def sortedInsert(self, head, x):
    #code here
    
        newnode = Node(x)
        
        cur = head
        
        if head.data > x:
            
            newnode.next = head
            
            head.prev = newnode
            
            return newnode
            
            
        while cur and cur.next:
            
            if cur.next.data>x:
                
                break
            
            cur = cur.next
            
            
        #insert the node
        
        newnode.next = cur.next
        
        newnode.prev = cur
        
        cur.next = newnode
        
        if newnode.next!=None:
            
            newnode.next.prev = newnode
            
            
        else:
            
            newnode.next = None
            
        return head
        
        
            
            
