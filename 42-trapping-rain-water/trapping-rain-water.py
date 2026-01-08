class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        prefixMax, suffixMax = [height[0]], [height[-1]]

        for i in range(1, n):
            prefixMax.append(max(prefixMax[-1], height[i]))

        for i in range(n - 2, -1, -1):
            suffixMax.append(max(suffixMax[-1], height[i]))

        for i in range(n):
            ans += max(0, min(prefixMax[i], suffixMax[n - i - 1]) - height[i])

        return ans