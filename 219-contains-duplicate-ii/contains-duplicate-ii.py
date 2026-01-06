class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        n = len(nums)

        for i in range(n):
            if nums[i] in seen:
                return True
                
            seen.add(nums[i])
            if i >= k:
                seen.remove(nums[i - k])
            
        return False
