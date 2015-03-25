__author__ = 'Vigery'


class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        n = 0
        while x // 10 ** n != 0:
            n += 1
        for i in range(n // 2):
            low = x % 10
            high = x // 10 ** (n - 1)
            if low != high:
                return False
            else:
                x = (x - high * 10 ** (n - 1)) // 10
                n -= 2
        return True

s = Solution()
print(s.isPalindrome(101))