import math

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        unique = list(set(nums))
        return [i for i in unique if nums.count(i)>math.floor(len(nums)/3)]