# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            #base case, no root exists, just add 0
            if not root:
                return 0
            
            #otherwise, compute making this the spit: this is then the global max
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(0, leftMax)
            rightMax = max(0, rightMax)
            res[0] = max(res[0], root.val + leftMax + rightMax)

            #now, return what we actually want to return, which is the value 
            #of hte maximum path by branching
            return root.val + max(dfs(root.left), dfs(root.right), 0)
        
        dfs(root)
        return res[0]
    

        

        