#User function Template for python3
#User function Template for python3

def quickSort(head):
    #return head after sorting
    
    
    def merge(list1,list2):

        if not list1 or not list2:

            return list1 or list2

        dummy=node=Node(0)

        while list1 and list2:

            if list1.data<list2.data:

                node.next=list1

                #=node.next

                list1=list1.next

            else:

                node.next=list2

                #node=node.next

                list2=list2.next

            node=node.next

        node.next=list1 or list2

        return dummy.next
            
            
    if not head or not head.next:
        
        return head
            
    
    
    fast = head.next
    
    slow = head
    
    while fast and fast.next:
        
        fast = fast.next.next
        
        slow = slow.next
        
    mid = slow.next
    
    slow.next = None
    
    list1 , list2 = quickSort(head) , quickSort(mid)
    
    return merge(list1,list2)

def quickSort(head):
    #return head after sorting
    
    
    def merge(list1,list2):

        if not list1 or not list2:

            return list1 or list2

        dummy=node=Node(0)

        while list1 and list2:

            if list1.data<list2.data:

                node.next=list1

                #=node.next

                list1=list1.next

            else:

                node.next=list2

                #node=node.next

                list2=list2.next

            node=node.next

        node.next=list1 or list2

        return dummy.next
            
            
    if not head or not head.next:
        
        return head
            
    
    
    fast = head.next
    
    slow = head
    
    while fast and fast.next:
        
        fast = fast.next.next
        
        slow = slow.next
        
    mid = slow.next
    
    slow.next = None
    
    list1 , list2 = quickSort(head) , quickSort(mid)
    
    return merge(list1,list2)