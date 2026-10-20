# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        res = dummy
        carry = 0
        while l1 and l2:
            v1 = l1.val
            v2 = l2.val 
            
            sum_val = v1 + v2 + carry
            if sum_val > 9:
                res.next = ListNode((sum_val % 10))
                carry = (sum_val // 10)
            else: 
                res.next = ListNode(sum_val)
                carry = 0
            
            l1 = l1.next
            l2 = l2.next
            res = res.next

        while l1:
            v1 = l1.val
            
            sum_val = v1 + carry
            if sum_val > 9:
                res.next = ListNode((sum_val % 10))
                carry = (sum_val // 10)
            else: 
                res.next = ListNode(sum_val)
                carry = 0
            l1 = l1.next
            res = res.next
        while l2:
            v2 = l2.val 
            
            sum_val = v2 + carry
            if sum_val > 9:
                res.next = ListNode((sum_val % 10))
                carry = (sum_val // 10)
            else: 
                res.next = ListNode(sum_val)
                carry = 0
            l2 = l2.next
            res = res.next
        
        if carry > 0:
            res.next = ListNode(carry)

        return dummy.next
        