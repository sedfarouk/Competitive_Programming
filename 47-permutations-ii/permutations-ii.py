class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        def backtrack():
            if len(curr) == n:
                solutions.add(tuple([nums[i] for i in curr]))
                return 

            for i in range(n):
                if i not in curr:
                    curr.append(i)
                    backtrack()
                    curr.pop()

        solutions, curr = set(), []
        backtrack()
        return [list(sol) for sol in solutions]