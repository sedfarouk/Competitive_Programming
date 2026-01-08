class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0

        left, right = 0, n - 1
        leftMax = rightMax = 0

        while left < right:
            if height[left] < height[right]:
                leftMax = max(leftMax, height[left])
                ans += leftMax - height[left]
                left += 1
            else:
                rightMax = max(rightMax, height[right])
                ans += rightMax - height[right]
                right -= 1
            
        return ans

        # prefixMax, suffixMax = [height[0]], [height[-1]]

        # for i in range(1, n):
        #     prefixMax.append(max(prefixMax[-1], height[i]))

        # for i in range(n - 2, -1, -1):
        #     suffixMax.append(max(suffixMax[-1], height[i]))

        # for i in range(n):
        #     ans += max(0, min(prefixMax[i], suffixMax[n - i - 1]) - height[i])

        # return ans