class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        hashmap = defaultdict(int)
        ans = 0

        for i in range(n):
            diff = nums[i] - i
            ans += hashmap[str(diff)]
            hashmap[str(diff)] += 1
        
        return n * (n - 1) // 2 - ans