"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        copies = {}

        def clone(node):
            # If node is created, reuse it
            if node in copies:
                return copies[node]
            
            # Create new node
            copy = Node(node.val)

            # Put in the map
            copies[node] = copy

            # Do the same for the neighbors
            for nb in node.neighbors:
                copy.neighbors.append(clone(nb))
            
            return copy
        
        return clone(node)