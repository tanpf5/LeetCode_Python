__author__ = 'Vigery'
from TreeNode import TreeNode

class Solution:
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


s = Solution()
t = TreeNode(3)
print(t.left)
print(s.isSameTree(t, t))