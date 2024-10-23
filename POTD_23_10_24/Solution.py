#User function Template for python3

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
        
        arr = []
        
        while head:
            
            arr.append(head.data)
            
            head = head.next
            
        return sum(arr[-n:])
            