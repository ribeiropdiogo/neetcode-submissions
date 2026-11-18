# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validNode(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):          # check this node against its range
                return False
            return (validNode(node.left, low, node.val) and    # left: values must be < node.val
                    validNode(node.right, node.val, high))     # right: values must be > node.val
        return validNode(root, float('-inf'), float('inf'))

# 
                
            