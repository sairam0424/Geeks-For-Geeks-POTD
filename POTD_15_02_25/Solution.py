'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    
    def LCA(self, root, n1, n2):
        
        while root:
        
            if n1.data <root.data and n2.data<root.data:
                
                root = root.left
                
            elif n1.data>root.data and n2.data>root.data:
                
                root = root.right
                
            else:
                
                return root
            
    


