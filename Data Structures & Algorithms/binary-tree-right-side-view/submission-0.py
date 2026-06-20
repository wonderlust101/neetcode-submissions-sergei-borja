# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def bfs(node, depth):
            if not node:
                return None
            
            if len(res) == depth:
                res.append(node.val)
            
            bfs(node.right, 1 + depth)
            bfs(node.left, 1 + depth)
        
        bfs(root, 0)
        return res

