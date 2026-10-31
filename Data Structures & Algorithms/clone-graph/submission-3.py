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
        
        copyToOld = {}

        def copy(node):
            if node in copyToOld:
                return copyToOld[node]
            
            newNode = Node(node.val)
            copyToOld[node] = newNode

            for nei in node.neighbors:
                newNode.neighbors.append(copy(nei))
            
            return newNode
        
        return copy(node)