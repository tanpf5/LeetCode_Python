__author__ = 'Vigery'


class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        p, q = head, head
        while p is not None and q is not None and q.next is not None:
            p = p.next
            q = q.next.next
            if p == q:
                return True
        return False