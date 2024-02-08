class Solution:
    def sortEvenOdd(self, A):
        A[1::2], A[::2] = sorted(A[1::2], reverse=True), sorted(A[::2])
        return A
        