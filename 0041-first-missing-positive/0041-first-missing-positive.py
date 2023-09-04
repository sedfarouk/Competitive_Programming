class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        unique = set(nums)
        maxx = max(nums)

        if maxx < 0:
            return 1
        
        for i in range(1, maxx+1):
            if i not in unique:
                return i
        return maxx+1

        


        