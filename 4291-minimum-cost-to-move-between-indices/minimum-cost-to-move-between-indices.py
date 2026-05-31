class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        prefA, prefB = [0] * n, [0] * n
        
        for i in range(n - 1):
            if i == 0 or (nums[i] - nums[i - 1]) > (nums[i + 1] - nums[i]):
                prefA[i + 1] = prefA[i] + 1
            else:
                prefA[i + 1] = prefA[i] + (nums[i + 1] - nums[i])

        for i in range(1, n):
            if i == n - 1 or (nums[i] - nums[i - 1]) <= (nums[i + 1] - nums[i]):
                prefB[i] = prefB[i - 1] + 1
            else:
                prefB[i] = prefB[i - 1] + (nums[i] - nums[i - 1])

        res = []
        for l, r in queries:
            if l < r:
                res.append(prefA[r] - prefA[l])
            else:
                res.append(prefB[l] - prefB[r])
            
        return res