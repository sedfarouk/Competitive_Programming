class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # suff = [1] * (n + 1)

        # for i in range(n - 1, -1, -1):
        #     suff[i] = suff[i + 1] * nums[i]

        # mul = 1
        # ans = []
        # for i in range(n):
        #     ans.append(mul * suff[i + 1])
        #     mul *= nums[i]

        # return ans

        ans = [0] * n
        ans[0] = 1

        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]

        r = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= r
            r *= nums[i]

        return ans
