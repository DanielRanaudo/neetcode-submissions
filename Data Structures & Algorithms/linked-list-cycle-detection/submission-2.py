# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sec = head
        while sec and head:
            sec = sec.next
            if sec == head:
                return True
            elif sec:
                sec = sec.next
                head = head.next
        return False