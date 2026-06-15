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
        # Create copy without random
        copy = Node(0)
        curr = copy
        random_hash = {}
        head_start = head

        while head:
            # create new node
            node = Node(head.val)

            random_hash[head] = node
            
            # move nodes ref
            curr.next = node
            curr = curr.next
            head = head.next

        head = head_start
        curr = copy.next
        while head and curr:
            if head.random:
                curr.random = random_hash[head.random]

            curr = curr.next
            head = head.next
            
        
        return copy.next