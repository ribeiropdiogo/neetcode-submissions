# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: 
        cur1, cur2 = l1, l2
        dummy = ListNode(0,None)
        cur = dummy
        excedent = 0
        while cur1 or cur2 or excedent:
            v1 = cur1.val if cur1 else 0
            v2 = cur2.val if cur2 else 0
            # New digit
            val = v1 + v2 + excedent
            excedent = val // 10
            val = val % 10
            cur.next = ListNode(val)
            # Update pointers
            cur = cur.next
            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None
        return dummy.next
            
