class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0

        for i in range(n - 1, 1, -1):
            start, end = 0, i - 1

            while start < end:
                if nums[start] + nums[end] > nums[i]:
                    ans += end - start
                    end -= 1
                else:
                    start += 1

        return ans