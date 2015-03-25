__author__ = 'Vigery'

class Solution:
    # @params strs, list of string
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        minlength = min(len(strs[i]) for i in range(len(strs)))
        if minlength == 0:
            return ''
        for i in range(minlength):
            s = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] != s:
                    return strs[0][:i]
        return strs[0][:minlength]

s = Solution()
print(s.longestCommonPrefix(['a', 'aa']))