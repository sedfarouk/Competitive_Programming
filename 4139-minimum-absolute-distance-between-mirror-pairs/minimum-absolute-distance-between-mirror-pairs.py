class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        h = defaultdict(lambda: float("-inf"))
        ans = float("inf")

        for idx, num in enumerate(nums):
            x = str(num)[::-1]
            ans = min(ans, idx - h[x])
            h[str(int(str(num)[::-1]))[::-1]] = idx

        return ans if ans != float("inf") else -1
            
            