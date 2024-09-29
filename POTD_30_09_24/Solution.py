#User function Template for python3
class Solution:
    def merge(self, root1, root2):
        # code here
        
        def dfs(root,arr):
            
            if not root:
                
                return 
            
            dfs(root.left,arr)
            
            arr.append(root.data)
            
            dfs(root.right,arr)
        
        arr = []
        
        dfs(root1,arr)
        
        dfs(root2,arr)
        
        return sorted(arr)
            