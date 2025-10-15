class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        prev = 0
        ans = cnt = 1
        n = len(nums)

        for i in range(1, n):
            if nums[i] > nums[i - 1]: cnt += 1
            else: 
                prev = cnt
                ans = max(ans, cnt // 2)
                cnt = 1

            ans = max(ans, min(cnt, prev))

        ans = max(ans, cnt // 2)
        return ans

