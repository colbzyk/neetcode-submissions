# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        res = dummy

        l1num = ""
        l2num = ""

        while l1 or l2:
            if l1:
                l1num += str(l1.val)
                l1 = l1.next
            if l2:
                l2num += str(l2.val)
                l2 = l2.next
        
        l1num = l1num[::-1]
        l2num = l2num[::-1]
        sum = int(l1num) + int(l2num)
        sumStr = str(sum)
        sumRev = sumStr[::-1]

        for i in range(len(sumStr)):
            res.next = ListNode(sumRev[i], None)
            res = res.next

        return dummy.next
            
