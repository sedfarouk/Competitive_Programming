class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        mxd = deque()
        ans = []

        for i in range(n):
            while mxd and (nums[mxd[-1]] <= nums[i]):
                mxd.pop()
            mxd.append(i)

            if i >= k - 1:
                ans.append(nums[mxd[0]])

            if mxd[-1] - mxd[0] >= k - 1:
                mxd.popleft()
        
        return ans



