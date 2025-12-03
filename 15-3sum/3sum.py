class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = set()

        for i in range(n):
            l, r = i + 1, n - 1

            while l < r:
                summ = nums[l] + nums[r] + nums[i]

                if summ == 0:
                    ans.add((nums[i], nums[l], nums[r]))
                if summ < 0:
                    l += 1
                else:
                    r -= 1

        return [list(x) for x in ans]