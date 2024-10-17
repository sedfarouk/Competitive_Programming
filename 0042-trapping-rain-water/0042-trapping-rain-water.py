class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0]
        suffix = [0]
        height = [0] + height[:]

        n = len(height)
        for i in range(n):
            prefix.append(max(prefix[-1], height[i]))

        for i in range(n-1, -1, -1):
            suffix.append(max(suffix[-1], height[i]))
        suffix.reverse()

        ans = 0
        for i in range(n):
            minn = min(prefix[i], suffix[i+1])

            if minn <= height[i]:
                continue
            ans += minn - height[i]
        return ans
        