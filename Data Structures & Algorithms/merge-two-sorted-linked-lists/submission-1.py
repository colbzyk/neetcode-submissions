# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return 
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        res = ListNode(None)
        cur = res

        while list1 is not None or list2 is not None:
            if list1 is None:
                cur.next = ListNode(list2.val)
                cur = cur.next
                list2 = list2.next
            elif list2 is None:
                cur.next = ListNode(list1.val)
                cur = cur.next
                list1 = list1.next
            else:
                lowest = min(list1.val, list2.val)
                cur.next = ListNode(lowest)
                cur =  cur.next

                if lowest == list1.val:
                    list1 = list1.next
                else:
                    list2 = list2.next
        

        return res.next
            