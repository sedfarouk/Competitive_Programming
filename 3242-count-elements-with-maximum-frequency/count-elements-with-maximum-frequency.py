class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = list(Counter(nums).values())
        mx = max(c)
        return mx * c.count(mx)
        