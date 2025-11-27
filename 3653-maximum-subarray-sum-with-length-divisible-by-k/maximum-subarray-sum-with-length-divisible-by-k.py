class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        pref = [0]

        for num in nums:
            pref.append(pref[-1] + num)

        ans = float("-inf")
        for i in range(k):
            summ = 0

            for j in range(i, len(nums) - k + 1, k):
                summ = max(summ + pref[j + k] - pref[j], pref[j + k] - pref[j])
                ans = max(ans, summ)

        return ans


