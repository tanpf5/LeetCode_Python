__author__ = 'Vigery'

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[k] = A[i]
                k -= 1
                i -= 1
            else:
                A[k] = B[j]
                k -= 1
                j -= 1
        if j >= 0:
            A[0:j + 1] = B[0:j + 1]
        return
