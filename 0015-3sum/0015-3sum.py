class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []

        for i in range(n):
            if i > 0 and nums[i-1] == nums[i]:
                continue

            l, r = i+1, n-1

            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                if summ == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1

                    while l < r and nums[l-1]==nums[l]:
                        l += 1

                elif summ > 0:
                    r -= 1
                
                else:
                    l += 1
        
        return list(ans)