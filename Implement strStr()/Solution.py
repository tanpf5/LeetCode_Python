__author__ = 'Vigery'

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            j, k = 0, i
            while j < len(needle) and k < len(haystack) and needle[j] == haystack[k]:
                j += 1
                k += 1
            if j == len(needle):
                return i
        return -1

s = Solution()
print(s.strStr('asbsdf', 'df'))