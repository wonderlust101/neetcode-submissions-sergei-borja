"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        mapping = {}
        res = Node(0)
        res_curr = res
        curr = head

        # Copy next 
        while curr:
            res_curr.next = Node(curr.val)
            mapping[curr] = res_curr.next

            curr = curr.next
            res_curr = res_curr.next
        
        curr = head
        res_curr = res.next
        while curr:
            if curr.random:
                res_curr.random = mapping[curr.random]
            
            curr = curr.next
            res_curr = res_curr.next

        return res.next