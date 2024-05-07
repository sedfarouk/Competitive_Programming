class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n==1: return True

        queue= deque([0])
        while queue:
            idx = queue.popleft()

            if nums[idx] > 0:
                maxx = idx
                for i in range(idx+1, min(idx + nums[idx]+1, n)):
                    if i==n-1:
                        return True
                    if i+nums[i] > nums[maxx]+maxx:
                        maxx = i
                if maxx!=idx:
                    queue.append(maxx)
          
        return False