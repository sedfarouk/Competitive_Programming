# 11. Leetcode - Container with most water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # BRUTE FORCE
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         h = min(height[i], height[j])
        #         ans = max(ans, h*(j-i))     
        # return ans 

        # OPTIMIZED SOLUTION
        ans = 0
        left, right = 0, len(height)-1

        while left < right:
            minn = min(height[left], height[right])
            ans = max(ans, minn*(right-left))

            if height[left] > height[right]:
                right-=1
            else:
                left+=1
        return ans
