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
        # Copy list first
        copy = Node(0)
        curr1 = copy
        curr2 = head
        random_map = {}

        while curr1 and curr2:
            new_node = Node(curr2.val)
            curr1.next = new_node
            random_map[curr2] = new_node

            curr1 = curr1.next
            curr2 = curr2.next

        curr1 = copy.next
        curr2 = head
        while curr1 and curr2:
            if curr2.random:
                curr1.random = random_map[curr2.random]
            
            curr1 = curr1.next
            curr2 = curr2.next
    
        return copy.next