# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        res_curr = res

        while list1 and list2:
            if list1.val < list2.val:
                res_curr.next = list1
                list1 = list1.next
            else:
                res_curr.next = list2
                list2 = list2.next

            res_curr = res_curr.next
        
        res_curr.next = list1 if list1 else list2

        return res.next