class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def possible_maxx(num):
            temp =nums[:]
            leftover = 0
            
            for i in range(len(temp)-1, 0, -1):
                leftover = max(0, temp[i]-num)
                temp[i-1] += leftover
            return temp[0] <= num
        
        l, r = 0, max(nums)
        ans = -1
        while l <= r:
            m = l + (r-l)//2
            
            if possible_maxx(m):
                ans = m
                r = m-1
            else:
                l = m+1
                
        return ans