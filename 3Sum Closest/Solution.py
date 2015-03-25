__author__ = 'Vigery'

class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        n = len(num)
        ans = num[0] + num[1] + num[2] - target
        for i in range(n - 2):
            sum2 = target - num[i]
            low, high = i + 1, n - 1
            while low < high:
                if num[low] + num[high] == sum2:
                    return target
                if abs(num[low] + num[high] - sum2) < abs(ans):
                    ans = num[low] + num[high] - sum2
                if num[low] + num[high] < sum2:
                    low += 1
                else:
                    high -= 1
        return ans + target
s = Solution()
a = [-3, -2, -5, 3, -4]
print(s.threeSumClosest(a, -1))