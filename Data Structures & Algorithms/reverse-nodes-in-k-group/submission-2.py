class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = k
        prev = None
        cur = head
        firstRun = True
        dummy = None
        tail = None

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

            count -= 1

            if count == 0:
                if firstRun:
                    dummy = prev
                    firstRun = False
                else:
                    tail.next = prev

                tail = head
                head.next = cur
                head = cur

                prev = None
                count = k

            # Reverse leftover nodes to restore original order
            if not cur and count != 0:
                cur = prev
                prev = None
                count = k - count

                while cur and count > 0:
                    tmp = cur.next
                    cur.next = prev
                    prev = cur
                    cur = tmp
                    count -= 1

                if tail:
                    tail.next = prev
                else:
                    dummy = prev

                return dummy

        return dummy
            
