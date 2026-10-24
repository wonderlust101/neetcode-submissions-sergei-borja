"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def copy(origNode):
            if origNode in oldToNew:
                return oldToNew[origNode]
            
            newNode = Node(origNode.val)
            oldToNew[origNode] = newNode

            for nbNode in origNode.neighbors:
                newNode.neighbors.append(copy(nbNode))
            
            return newNode
        
        return copy(node) if node else None