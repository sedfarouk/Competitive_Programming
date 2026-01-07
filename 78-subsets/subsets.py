class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subset = []
        res = []

        def backtrack(i):
            if i == n:
                res.append(subset[:])
                return 

            backtrack(i + 1)
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()

        backtrack(0)
        return res