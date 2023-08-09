# 1732. Leetcode - Find The Highest Altitude

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum = [0]

        for i in gain:
            prefix_sum.append(prefix_sum[-1]+i)
        return max(prefix_sum)
