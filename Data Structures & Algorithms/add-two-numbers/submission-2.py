# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1, l2
        res = ListNode()
        curr = res

        carry = 0
        while curr1 or curr2 or carry:
            a = curr1.val if curr1 else 0
            b = curr2.val if curr2 else 0

            sum = a + b + carry

            val = sum % 10
            carry = sum // 10
            curr.next = ListNode(val)

            curr = curr.next
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None


        return res.next