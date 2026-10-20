# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # Get maxDepth of each child
        maxleft = self.maxDepth(root.left)
        maxright = self.maxDepth(root.right)
        # Calculate max depth
        return 1 + max(maxleft,maxright)
        