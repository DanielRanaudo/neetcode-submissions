"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def createCopy(node: Optional['Node']):
            curr = Node(node.val)
            return curr

        #assuming the node is already unique
        def helper(node: Optional['Node'], ogNeighbors):
            if not node:
                return
            for v in ogNeighbors:
                if v in visited:
                    node.neighbors.append(visited[v])

                else: 
                    newNeigh = createCopy(v)
                    node.neighbors.append(newNeigh)
                    visited[v] = newNeigh
                    helper(newNeigh, v.neighbors)
            

        if not node:
            return None

        root = Node(node.val)
        visited[node] = root
        helper(root, node.neighbors)
        return root