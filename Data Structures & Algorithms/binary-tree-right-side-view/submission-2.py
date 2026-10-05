# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level = []

        def dfs(root, lvl):
            if not root:
                return None

            if len(level) == lvl:
                level.append(root.val)
            
            dfs(root.right, lvl + 1)
            dfs(root.left, lvl + 1)
        
        dfs(root, 0)
        return level