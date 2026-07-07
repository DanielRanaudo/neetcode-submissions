# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return self.helper(1, root)

    def helper(self, depth: int, root: Optional[TreeNode]) -> int:
        if root.left == None and root.right == None:
            return depth

        leftDepth = depth + 1
        rightDepth = depth + 1
        if (root.left != None):
            leftDepth = self.helper(leftDepth, root.left)
        if (root.right != None):
            rightDepth = self.helper(rightDepth, root.right)
        
        return max(leftDepth, rightDepth)


        

        