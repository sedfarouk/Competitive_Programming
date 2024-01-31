class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(state, total, idx):
            if total==target:
                solutions.append(state.copy())
                return

            for i in range(idx, len(candidates)):
                if i!=idx and candidates[i]==candidates[i-1]:
                    continue
                if total + candidates[i] <= target:
                    backtrack(state + [candidates[i]], total + candidates[i], i+1)

        candidates.sort()
        solutions = []
        backtrack([], 0, 0)
        return solutions

        
