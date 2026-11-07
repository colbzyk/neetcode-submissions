# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        res = dummy

        carry = 0

        while l1 or l2 or carry:
            if l1:
                l1num = l1.val
                l1 = l1.next
            else:
                l1num = 0
            if l2:
                l2num = l2.val
                l2 = l2.next
            else:
                l2num = 0

            val = l1num + l2num + carry
            carry = val // 10
            val = val % 10
            res.next = ListNode(val, None)
            res = res.next

        return dummy.next
            
