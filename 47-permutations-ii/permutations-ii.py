class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        candidates = Counter(nums)

        def backtrack():
            if len(curr) == n:
                solutions.append(curr.copy())
                return 

            for num in candidates:
                if candidates[num] > 0:
                    candidates[num] -= 1
                    curr.append(num)
                    backtrack()
                    curr.pop()
                    candidates[num] += 1

        solutions, curr = [], []
        backtrack()
        return solutions