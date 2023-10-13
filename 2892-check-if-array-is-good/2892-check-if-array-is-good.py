class Solution:
    def isGood(self, nums: List[int]) -> bool:
        count = Counter(nums)

        maxx = max(nums)

        if len(nums) < maxx + 1:
            return False

        for i in range(len(nums)):
            if nums[i] != maxx and count[nums[i]] > 1:
                return False
            elif nums[i]==maxx and count[maxx] != 2:
                return False
        
        return True

        