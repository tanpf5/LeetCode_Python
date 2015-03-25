__author__ = 'Vigery'


class Solution:
    # @return a string
    def convert(self, s, nRows):
        # x is the interval of two characters
        if nRows == 1:
            x = 1
        else:
            x = (nRows - 1) * 2
        i = 0
        ans = ''
        while i < nRows:
            for c in range(0, len(s), x):
                j = c + i
                if j < len(s):
                    ans += s[j]
                if i != 0 and i != nRows - 1:
                    k = c + x - i
                    if k < len(s):
                        ans += s[k]
            i += 1
        return ans

s = Solution()
print(s.convert("ABCDE", 4))