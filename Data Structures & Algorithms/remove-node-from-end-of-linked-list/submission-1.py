# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        current = head

        while current:
            size += 1
            current = current.next

        target = size - n

        if target == 0:
            return head.next
        
        current, prev = head, None
        while current:
            if target == 0:
                prev.next = current.next
            prev = current
            current = current.next
            target -= 1

        return head