"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        copies = {}

        def copy(node):
            # If node already exist, return it from memory
            if node in copies:
                return copies[node]
            
            # Create new node
            new = Node(node.val)
            copies[node] = new

            # Copy neighbors
            for n in node.neighbors:
                new.neighbors.append(copy(n))
            
            return new
        
        return copy(node)