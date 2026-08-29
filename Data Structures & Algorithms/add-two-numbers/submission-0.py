# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        cur = dummy
        carry = 0
        while l1 or l2 or carry != 0:
            
            summ = (0 if not l1 else l1.val) + (0 if not l2 else l2.val) + carry
            carry = summ // 10
            digit = summ % 10
            cur.next = ListNode(digit, None)
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
            cur = cur.next
        return dummy.next
        