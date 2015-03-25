__author__ = 'Vigery'

from ListNode import ListNode

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        n1 = head
        while n1 is not None:
            n1 = n1.next
            n2 = head
            while n2 != n1 and n2.val <= n1.val:
                n2 = n2.next
            if n2 != n1:



n = ListNode(3)
