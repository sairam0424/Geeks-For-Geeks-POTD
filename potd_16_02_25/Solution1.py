#User function Template for python3


'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
a=[]
class Solution:
    #Function to serialize a tree and return a list containing nodes of tree.
    def serialize(self, root):
        #code here
        
        global a
        
        if not root:
            
            a.append('!')
            
            return a
        
        a.append(root.data)
        
        self.serialize(root.left)
        
        self.serialize(root.right)
        
        return a
        #return a
        
    
    #Function to deserialize a list and construct the tree.   
    def deSerialize(self, a):
        #code here
    
        node=a.pop(0)
        
        if node=="!":
            
            return None
            
        root=Node(node)
        
        root.left=self.deSerialize(a)
        
        root.right=self.deSerialize(a)
        
        return root

