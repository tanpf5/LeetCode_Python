__author__ = 'Vigery'

class Solution:
    # @return an integer
    def atoi(self, str):
        if not str:
            return 0
        str = str.strip(' ')
        if not str:
            return 0
        INT_MAX = 2 ** 31 - 1
        INT_MIN = 2 ** 31 * -1
        n = 1
        if str[0] == '-':
            sign = -1
        elif str[0] == '+' or str[0].isdigit():
                sign = 1
                if str[0].isdigit():
                    n = 0
        else:
            return 0
        ans = 0
        while n < len(str) and str[n].isdigit():
            digit = int(str[n])
            if sign == 1:
                if ans < INT_MAX // 10 or (ans == INT_MAX // 10 and digit <= INT_MAX % 10):
                    ans = ans * 10 + digit
                else:
                    return INT_MAX
            elif ans < INT_MAX // 10 or (ans == INT_MAX // 10 and digit <= 8):
                ans = ans * 10 + digit
            else:
                return INT_MIN
            n += 1
        return ans * sign
ss = Solution()
print(ss.atoi('    010'))