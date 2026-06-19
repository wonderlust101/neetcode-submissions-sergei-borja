# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        res_curr = res

        carry = 0
        while l1 or l2:
            a, b = 0, 0
            if l1:
                a = l1.val
                l1 = l1.next
            if l2:
                b = l2.val
                l2 = l2.next
            
            sum = a + b + carry

            carry = sum // 10
            remainder = sum % 10

            res_curr.next = ListNode(remainder)

            res_curr = res_curr.next

        if carry > 0:
            res_curr.next = ListNode(carry)

        return res.next