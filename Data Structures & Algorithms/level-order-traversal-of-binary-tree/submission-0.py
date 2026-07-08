# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #bfs using queue
        queue = deque() 
        queue.append(root)

        res = []
        pos = 0
        while(queue):
            level = []
            temp = deque()
            while (queue):
                elm = queue.popleft()
                #pop everything in queue, adding all its children
                if (elm):
                    temp.append(elm.left)
                    temp.append(elm.right)
                    level.append(elm.val)
            if len(level) > 0:
                res.append(level)
            queue = temp
            pos += 1
        
        return res
        