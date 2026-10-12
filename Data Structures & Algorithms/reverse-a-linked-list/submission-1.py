# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return
        current = ListNode(head.val)

        while head.next != None:
            current = ListNode(head.next.val, current)
            head = head.next

        return current