#User function Template for python3
'''
class DLLNode:
    def __init__(self,val) -> None:
        self.data = val
        self.prev = None
        self.next = None
'''
from heapq import heappop,heappush
class Solution:
    def sortAKSortedDLL(self, head, k):
        # Code Here
        p = q = head
        h = []
        while q:
            heappush(h, q.data)
            if len(h) >= k+1:
                p.data = heappop(h)
                p = p.next
            q = q.next
        while h:
            p.data = heappop(h)
            p = p.next
        return head