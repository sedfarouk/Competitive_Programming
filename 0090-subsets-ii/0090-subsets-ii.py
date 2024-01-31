class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(state, idx):
            solutions.append(state.copy())

            for i in range(idx, len(nums)):
                if i!= idx and nums[i]==nums[i-1]:
                    continue
                backtrack(state + [nums[i]], i+1)

        nums.sort()
        solutions = []
        backtrack([], 0)
        return solutions
