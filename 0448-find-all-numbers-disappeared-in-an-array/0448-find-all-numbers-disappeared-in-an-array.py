class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        perm = set([i for i in range(1, len(nums)+1)])
        return perm.difference(set(nums))
        