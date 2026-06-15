# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Get Length
        length = 0

        curr = head
        while curr:
            curr = curr.next
            length += 1

        # Get index
        remove_index = length - n

        # Remove Head
        if remove_index == 0:
            return head.next

        # Remove middle index
        curr = head
        for _ in range(remove_index - 1):
            curr = curr.next
    
        curr.next = curr.next.next

        return head