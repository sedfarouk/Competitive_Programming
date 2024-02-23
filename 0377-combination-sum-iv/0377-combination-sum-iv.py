class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target+1)
        dp[target] = 1

        for i in range(target, -1, -1):
            for num in nums:
                if i+num <= target:
                    dp[i] += dp[i+num]
        return dp[0]

        # memo = {}

        # def dp(total):
        #     if total in memo: return memo[total]
        #     if total==target: return 1

        #     ans = 0
        #     for num in nums:
        #         if (num+total) <= target:
        #             ans += dp(total+num)
        #     memo[total] = ans
        #     return memo[total]
        # return dp(0)
            
