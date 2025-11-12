class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)

        if ones > 0: return n - ones

        ans = float("inf")
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = gcd(g, nums[j])

                if g == 1:
                    ans = min(ans, j - i + n - 1)
                    break

        return ans if ans != float("inf") else -1

