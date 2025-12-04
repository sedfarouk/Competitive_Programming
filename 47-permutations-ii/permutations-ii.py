class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        candidates = set([*range(n)])

        def backtrack():
            if len(curr) == n:
                solutions.add(tuple([nums[i] for i in curr]))
                return 

            for i in list(candidates):
                candidates.remove(i)
                curr.append(i)
                backtrack()
                curr.pop()
                candidates.add(i)

        solutions, curr = set(), []
        backtrack()
        return [list(sol) for sol in solutions]