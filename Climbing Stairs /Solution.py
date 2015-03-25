__author__ = 'Vigery'


class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        i, j = 1, 2
        for k in range(3, n + 1):
            i, j = j, i + j
        return j

s = Solution()
print(s.climbStairs(10))