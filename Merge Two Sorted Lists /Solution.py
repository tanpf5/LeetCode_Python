__author__ = 'Vigery'

from ListNode import ListNode

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val <= l2.val:
            l = ListNode(l1.val)
            l1 = l1.next
        else:
            l = ListNode(l2.val)
            l2 = l2.next
        ans = l
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                l.next = ListNode(l1.val)
                l = l.next
                l1 = l1.next
            else:
                l.next = ListNode(l2.val)
                l = l.next
                l2 = l2.next
        if l1 is not None:
            l.next = l1
        else:
            l.next = l2
        return ans

s = Solution()
l3 = ListNode(1)
l3.next = ListNode(2)
l3.next.next = ListNode(4)
l4 = ListNode(5)
ll = s.mergeTwoLists(l3, l4)
while ll is not None:
    print(ll.val)
    ll = ll.next