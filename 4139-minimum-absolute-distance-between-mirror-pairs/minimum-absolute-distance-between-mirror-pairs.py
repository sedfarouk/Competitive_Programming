class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        h = defaultdict(lambda: float("-inf"))
        ans = float("inf")

        def reverseNum(num):
            rev = 0

            while num > 0:
                rev = rev * 10 + (num % 10)
                num //= 10
            
            return rev

        for idx, num in enumerate(nums):
            ans = min(ans, idx - h[num])
            h[reverseNum(num)] = idx

        return ans if ans != float("inf") else -1
            
            