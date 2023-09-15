class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n+1

        while left + 1 < right:
            mid = left + (right - left) // 2

            if mid*int((mid+1))/2 <= n:
                left = mid
            else:
                right = mid

        return left













































































