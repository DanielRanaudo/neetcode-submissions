# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = list1, list2
        res = ListNode()
        resCur = res
        while curr1 and curr2:
            if curr1.val >= curr2.val:
                resCur.next = curr2
                curr2 = curr2.next
            elif curr2.val > curr1.val:
                resCur.next = curr1
                curr1 = curr1.next
            resCur = resCur.next

        #attach the rest if one is larger thant the other
        if curr1:
            resCur.next = curr1
        elif curr2:
            resCur.next = curr2
            
        return res.next



        