class Solution:
    def isGood(self, nums: List[int]) -> bool:
        count = Counter(nums)
        n = len(nums)-1
        return all(count[i]==1 for i in range(1, n)) and count[n]==2
        