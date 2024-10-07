def insert(head,data):
    
    new_node = Node(data)
    
    new_node = new_node.npx
    
    return new_node


def getList(head):
    
    res = []
    
    while head:
        
        res.append(head.data)
        
        head = head.npx
        
    return res