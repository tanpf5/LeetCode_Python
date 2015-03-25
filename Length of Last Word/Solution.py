__author__ = 'Vigery'

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        if s == '':
            return 0
        s = s.rstrip(' ')
        i = s.rfind(' ')
        if i == -1:
            return len(s)
        return len(s) - i - 1


so = Solution()
ss = 'workdhel23lo  '
print(so.lengthOfLastWord(ss))