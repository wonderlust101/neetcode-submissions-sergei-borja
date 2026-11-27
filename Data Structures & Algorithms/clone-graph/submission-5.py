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
        
        copy = {}
        
        def dfs(node):
            if node in copy:
                return copy[node]
            
            nodeCopy = Node(node.val)
            copy[node] = nodeCopy

            for nodeNei in node.neighbors:
                nodeCopy.neighbors.append(dfs(nodeNei))
            
            return nodeCopy
        
        dfs(node)
        return copy[node]