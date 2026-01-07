class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = curr = 0
        h = defaultdict(int)
        h[0] = 1

        for num in nums:
            curr += num
            ans += h[curr - k]
            h[curr] += 1

        return ans