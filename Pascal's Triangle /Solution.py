__author__ = 'Vigery'

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows < 1:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        ans = [[1], [1, 1]]
        a = [1, 1]
        for i in range(3, numRows + 1):
            b = [1]
            for j in range(i - 2):
                b.append(a[j] + a[j + 1])
            b.append(1)
            ans.append(b)
            a = b
        return ans

s = Solution()
print(s.generate(5))