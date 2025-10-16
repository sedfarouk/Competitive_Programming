class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mods = Counter([num % value for num in nums])

        for i in range(len(nums)):
            if mods[i % value] == 0:
                return i
            mods[i % value] -= 1
        return len(nums)
