#User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    # Function to reverse a circular linked list
    def reverse(self, head):
        # easy way
        arr = [head.data]
        temp = head.next
        while temp!=head:
            arr.append(temp.data)
            temp = temp.next
        temp = head
        for element in arr[::-1]:
            temp.data = element
            temp = temp.next
        return head
        
    # Function to delete a node from the circular linked list
    def deleteNode(self, head, key):
        prev = head
        temp = head.next
        
        # Find tail
        tail = head
        while temp != head:
            temp = temp.next
            tail = tail.next
            
        # If head is key, set tail to the element next of head
        if head.data == key:
            tail.next = head.next
            head = head.next
            return head
            
        # If head is not key
        temp = head.next
        while temp != head:
            if temp.data == key:
                prev.next = temp.next
                temp = temp.next
                break
            prev = prev.next
            temp = temp.next
        return head
        
