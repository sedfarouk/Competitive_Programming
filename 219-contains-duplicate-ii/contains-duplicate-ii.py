class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h = defaultdict(int)
        n = len(nums)

        for i in range(n):
            if nums[i] in h and i - h[nums[i]] <= k:
                return True
            h[nums[i]] = i
        return False
