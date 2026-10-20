# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True

        def dfs(root) -> int:
            nonlocal res
            if not root:
                return 0
            # Get max height of children
            maxL = dfs(root.left)
            maxR = dfs(root.right)
            # Check if diff > 1
            if maxL - maxR < -1 or maxL - maxR > 1:
                res = False
            # Return height
            return 1 + max(maxL,maxR)
        
        dfs(root)

        return res