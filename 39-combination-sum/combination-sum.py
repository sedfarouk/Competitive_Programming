class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        curr = []

        def combination(idx, s):
            if s == target:
                solutions.append(curr[:])
                return

            for i in range(idx, n):
                k = candidates[i]
                if s + k <= target:
                    curr.append(k)
                    combination(i, s + k)
                    curr.pop()

        solutions = []
        combination(0, 0)
        return solutions