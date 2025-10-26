class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        ans = curr = 0
        h = defaultdict(int)
        h[0] = 1
        
        for i in range(len(nums)):
            curr += nums[i]
            ans += h[curr % k]
            h[curr % k] += 1

        for x, it in groupby(nums):
            l = len(list(it))
            c = 0

            for i in range(l):
                c += x
                if c % k == 0:
                    ans -= (l - (i + 1))

        return ans

        
        