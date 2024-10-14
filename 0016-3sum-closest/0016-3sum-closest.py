class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = float('inf')
        n = len(nums)
        nums.sort()

        for i in range(n-2):
            l, r = i+1, n-1

            while l < r:
                curr = nums[i] + nums[l] + nums[r]
                if abs(curr - target) < abs(ans - target):
                    ans = curr

                if curr == target:
                    return ans

                elif curr < target:
                    l += 1
                else:
                    r -= 1
        return ans

