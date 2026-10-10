# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightView = []

        def dfs(node, lvl):
            if not node:
                return None

            if len(rightView) == lvl:
                rightView.append(node.val)
            
            dfs(node.right, lvl + 1)
            dfs(node.left, lvl + 1)
        
        dfs(root, 0)
        return rightView
            