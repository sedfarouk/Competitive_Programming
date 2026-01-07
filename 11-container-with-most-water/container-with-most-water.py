class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        res = 0

        while l < r:
            mn = min(height[l], height[r])
            res = max(res, (r - l) * mn)

            if height[l] > mn:
                r -= 1
            else:
                l += 1

        return res