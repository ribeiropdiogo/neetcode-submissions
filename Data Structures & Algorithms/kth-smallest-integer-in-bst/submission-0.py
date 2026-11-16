# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        
        def dfs(node):
            if not node or len(res) >= k:   # stop early
                return
            dfs(node.left)              # search left subtree
            if len(res) < k:
                res.append(node.val)    # include node itself
            dfs(node.right)             # search right subtree
        dfs(root)
        return res[k-1]
# 
# Travers tree in-order df and store up to k elements
#