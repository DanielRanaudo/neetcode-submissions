# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        max_val = float('inf')
        min_val = float('-inf')
        return self.helper(root, max_val, min_val)


    def helper(self, root: Optional[TreeNode], maxim: float, minim: float) -> bool:
        #base case
        if not root:
            return True
        
        if minim < root.val < maxim:
            #left should contain root.val as max, keep min, 
            #right should contain root.val as min, keep max
            return self.helper(root.left, root.val, minim) and self.helper(root.right, maxim, root.val)
        else: 
            return False

        