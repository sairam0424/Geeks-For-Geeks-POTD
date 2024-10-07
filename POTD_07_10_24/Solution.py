def insert(head, data):
    
    new_node = Node(data)
    
    new_node.npx = head
    
    return new_node
    
def getList(head):
    
    res = []
    
    while head:
        
        res.append(head.data)
        
        head = head.npx
        
    return res