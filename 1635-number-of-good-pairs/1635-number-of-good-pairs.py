class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(sum(range(i)) for i in Counter(nums).values())
 
