"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copys = {}

        cur = head

        while cur:
            copy = Node(cur.val)
            copys[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = copys[cur]
            copy.next = copys.get(cur.next)
            copy.random = copys.get(cur.random)
            cur = cur.next

        return copys.get(head)
