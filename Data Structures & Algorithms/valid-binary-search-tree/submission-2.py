# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validNode(node,low,high):
            if not node:
                return True
            if node.left:
                if node.val <= node.left.val:
                    return False
            if node.right:
                if node.val >= node.right.val:
                    return False
            if low < node.val < high:
                return validNode(node.left,low,node.val) and validNode(node.right,node.val,high)
            else:
                return False
        return validNode(root,float('-inf'),float('inf'))

# 
                
            