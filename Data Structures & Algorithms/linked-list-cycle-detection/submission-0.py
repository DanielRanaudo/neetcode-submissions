# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        prev = set() #stores previous nodes
        while head:
            if head in prev:
                return True
            else:
                prev.add(head)
            
            head = head.next
        return False


        