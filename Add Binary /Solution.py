__author__ = 'Vigery'

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        ans = ''
        la, lb = len(a), len(b)
        g = 0
        for i in range(max(la, lb)):
            if la - 1 - i < 0:
                x = 0
            else:
                x = int(a[la - 1 - i])
            if lb - 1 - i < 0:
                y = 0
            else:
                y = int(b[lb - 1 - i])
            ans += str((x + y + g) % 2)
            g = (x + y + g) // 2
        if g == 1:
            ans += str(g)
        return ans[::-1]

s = Solution()
a = '11'
b = '1'
print(s.addBinary(a, b))