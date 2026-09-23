# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0

        curr = head
        while curr:
            i += 1
            curr = curr.next
        
        removeIndex = i - n

        if removeIndex == 0:
            return head.next

        curr = head
        for i in range(removeIndex - 1):
            curr = curr.next
        
        temp = curr.next.next
        curr.next = temp

        return head