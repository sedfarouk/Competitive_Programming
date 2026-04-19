class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        h = {}
        ans = 1000000

        def reverseNum(num):
            rev = 0

            while num > 0:
                rev = rev * 10 + (num % 10)
                num //= 10
            
            return rev

        for idx, num in enumerate(nums):
            if num in h:
                ans = min(ans, idx - h[num])
            h[reverseNum(num)] = idx

        return ans if ans != 1000000 else -1
            
            