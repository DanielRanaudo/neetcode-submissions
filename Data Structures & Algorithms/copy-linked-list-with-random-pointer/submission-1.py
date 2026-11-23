"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        dummy = Node(0)
        curr = dummy 

        realCopy = head

        mapping = {} #

        #iterate through
        while head:
            curr.val = head.val

            if head.next:
                nextVal = head.next.val
                curr.next = Node(nextVal)

            curr.random = None

            mapping[head] = curr
            
            curr = curr.next 
            head = head.next 

        curr = dummy
        head = realCopy

        while head:
            if head.random:
                curr.random = mapping[head.random]

            head = head.next 
            curr = curr.next 
        return dummy
            





        