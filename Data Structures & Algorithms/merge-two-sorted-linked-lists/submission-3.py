# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        node = res
        curr1, curr2 = list1, list2

        while curr1 and curr2:
            if curr1.val < curr2.val:
                node.next = curr1
                node = node.next
                curr1 = curr1.next
            else:
                node.next = curr2
                node = node.next
                curr2 = curr2.next

        if curr1:
            node.next = curr1
        else:
            node.next = curr2

        return res.next