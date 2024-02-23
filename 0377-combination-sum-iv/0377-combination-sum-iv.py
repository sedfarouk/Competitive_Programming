class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(total):
            if total in memo: return memo[total]
            if total==target: return 1

            ans = 0
            for num in nums:
                if (num+total) <= target:
                    ans += dp(total+num)
            memo[total] = ans
            return memo[total]
        return dp(0)
            
