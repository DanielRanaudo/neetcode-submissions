# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root

        if root.right != None or root.left != None:
            right = root.right
            left = root.left

            root.right = left
            root.left = right

            self.invertTree(right)
            self.invertTree(left)
        
        return root

        