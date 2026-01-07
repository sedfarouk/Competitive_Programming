class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suff = [1] * (n + 1)

        for i in range(n - 1, -1, -1):
            suff[i] = suff[i + 1] * nums[i]

        mul = 1
        ans = []
        for i in range(n):
            ans.append(mul * suff[i + 1])
            mul *= nums[i]

        return ans
