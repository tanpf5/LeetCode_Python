__author__ = 'Vigery'

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        return self.pathSum2(root, sum, [[]])

    # @param root, a tree node
    # @param sum, an integer
    # @param result, a list of lists of integers
    # @return a list of lists of integers
    def pathSum2(self, root, sum, result):
        if root is None:
            return result
        if root.left is not None:
            self.pathSum2(root.left, sum - root.val, result)
        if root.right