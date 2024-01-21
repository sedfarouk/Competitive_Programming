class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        ans = 0
        nums = [a, b, c]

        while nums.count(0) < 1:
            min_idx = nums.index(min(nums))
            nums[min_idx] -= 1
            max_idx = nums.index(max(nums))
            nums[max_idx] -= 1

            ans += 1
            if nums.count(0)==1:
                return min(nums[:min_idx]+nums[min_idx+1:]) + ans
            
        return ans

        