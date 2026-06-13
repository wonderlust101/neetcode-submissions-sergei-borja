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
            length +=1
            curr = curr.next
        
        remove_index = length - n

        if remove_index == 0:
            return head.next

        remove_curr = head
        for _ in range(remove_index - 1):
            remove_curr = remove_curr.next
        
        remove_curr.next = remove_curr.next.next

        return head