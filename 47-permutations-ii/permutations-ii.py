class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        cnt = Counter(nums)
        curr = []
        u = list(cnt.keys())

        def backtrack():
            if len(curr) == n:
                solutions.append(copy.copy(curr))
                return

            for k in u:
                if cnt[k] > 0:
                    cnt[k] -= 1
                    curr.append(k)
                    backtrack()
                    cnt[k] += 1
                    curr.pop()

        solutions = []
        backtrack()
        return solutions

