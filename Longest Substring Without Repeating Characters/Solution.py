__author__ = 'Vigery'

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        ans = 0
        low = 0
        d = {}
        for high in range(len(s)):
            if d.__contains__(s[high]):
                low = max(d.pop(s[high]) + 1, low)
                d.__setitem__(s[high], high)
            else:
                d.__setitem__(s[high], high)
            if high - low + 1 > ans:
                    ans = high - low + 1
        return ans
