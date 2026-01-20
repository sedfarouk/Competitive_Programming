class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            for j in range(num):
                if (j | j + 1) == num:
                    ans.append(j)
                    break
            else:
                ans.append(-1)

        return ans