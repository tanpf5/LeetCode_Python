__author__ = 'Vigery'


class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        count = 0
        for i in range(1, len(A)):
            if A[i] == A[i - 1]:
                count += 1
            else:
                A[i - count] = A[i]
        return len(A) - count



s = Solution()
A = [0, 1, 2, 2, 2, 2, 3, 3, 4, 5, 6, 7, 7, 7, 7, 8]
print(s.removeDuplicates(A))