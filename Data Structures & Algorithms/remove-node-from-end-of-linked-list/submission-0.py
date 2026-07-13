# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1 
            curr = curr.next
        #Make the lone node case
        if length == 1:
            return None
        #Nth = length case
        if n == length:
            return head.next

        curr = head
        nth = length
        dummy = ListNode()
        dummy.next = head
        while curr:
            nth -= 1
            if n == nth:
                curr.next = curr.next.next
                break
            curr = curr.next
        return dummy.next
        