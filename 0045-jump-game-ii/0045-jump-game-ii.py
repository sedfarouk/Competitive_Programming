class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        queue = deque([(0, 0)])
        ans = float("inf")
        vis = set()

        while queue:
            idx, s = queue.popleft()

            if idx==n-1:
                return s

            for i in range(idx+1, min(idx+nums[idx]+1, n)):
                if i not in vis and i <= n-1:
                    queue.append((i, s+1))
                    vis.add(i)
        
        return ans

        # @lru_cache(None)
        # def dp(i):
        #     if i>=len(nums)-1:
        #         return 0

        #     minn = float("inf")
        #     if nums[i] > 0:
        #         for j in range(i+1, i+nums[i]+1):
        #             minn = min(minn, dp(j) + 1)
        #     return minn

        # return dp(0)