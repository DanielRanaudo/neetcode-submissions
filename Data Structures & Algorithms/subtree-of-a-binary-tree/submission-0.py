# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #recursive searchmode, always check if it exists
        if not root:
            return False
        if self.subtreeCheck(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def subtreeCheck(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root and not subRoot:
            return False
        
        #else, keep checking
        if root.val != subRoot.val:
            return False

        return self.subtreeCheck(root.left, subRoot.left) and self.subtreeCheck(root.right, subRoot.right)
        

        