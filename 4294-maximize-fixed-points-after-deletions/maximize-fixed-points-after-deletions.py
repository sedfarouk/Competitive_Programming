class Solution:
    def maxFixedPoints(self, nums: list[int]) -> int:
        n = len(nums)
        arr = []
        lis = []

        for i in range(n):
            d = i - nums[i]
            if d >= 0: arr.append((d, nums[i]))

        arr.sort()
        for d, x in arr:
            if not lis or x > lis[-1]:
                lis.append(x)
            else:
                lis[bisect_left(lis, x)] = x 
            
        return len(lis)