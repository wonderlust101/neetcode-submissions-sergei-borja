# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        sp,fp = head, head

        # Get Center
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next

        # Reverse List
        prev, curr = None, sp.next
        sp.next = None
        while curr:
            next_ref = curr.next
            curr.next = prev
            prev = curr
            curr = next_ref
        
        # Reorder List - combine head and prev
        list1, list2 = head, prev
        while list1 and list2:
            temp1, temp2 = list1.next, list2.next
            list1.next = list2
            list2.next = temp1
            list1, list2 = temp1, temp2