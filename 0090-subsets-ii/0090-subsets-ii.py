class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(state, idx):
            solutions.append(state.copy())

            for i in range(idx, len(keys)):
                if count[keys[i]] > 0:
                    count[keys[i]] -= 1
                    backtrack(state+[keys[i]], i)
                    count[keys[i]] += 1

        solutions = []
        count = Counter(nums)
        keys = list(count.keys())
        backtrack([], 0)
        return solutions
