# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []

        def bfs(node, max_val):
            if not node:
                return None

            if node.val >= max_val:
                res.append(node.val)
            
            bfs(node.left, max(node.val, max_val))
            bfs(node.right, max(node.val, max_val))
        
        bfs(root, root.val)
        return len(res)


