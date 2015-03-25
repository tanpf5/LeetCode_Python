__author__ = 'Vigery'


class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        for i in range(k):
            nums.insert(0, nums.pop(len(nums) - 1))
        return

s = Solution()
a = [1, 2, 3, 4, 5, 6, 7]
s.rotate(a, 3)
print(a)