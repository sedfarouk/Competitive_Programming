class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()

        # curr, ans = 0, float("inf")
        # tot = sum(nums)

        # for i in range(1, n + 1):
        #     curr += nums[i - 1]
        #     tot -= nums[i - 1]
        #     ans = min(ans, tot - curr + nums[i - 1] * (2 * i - n))
    
        # return ans

        # Using concept of | x - min | + |x - max | = max - min
        ans = 0
        for i in range(n // 2):
            ans += nums[n - i - 1] - nums[i]
        return ans
