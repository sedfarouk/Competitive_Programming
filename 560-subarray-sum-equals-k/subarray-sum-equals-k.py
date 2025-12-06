class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        h = defaultdict(int)
        h[0] = 1
        ans = curr = 0

        n = len(nums)
        for i in range(n):
            curr += nums[i]
            ans += h[curr - k]
            h[curr] += 1

        return ans