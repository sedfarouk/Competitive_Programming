class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans=0
        nums.sort()

        temp = 1
        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]:
                temp += 1
            else:
                ans += sum(range(temp))
                temp = 1
        ans += sum(range(temp))
        
        return ans