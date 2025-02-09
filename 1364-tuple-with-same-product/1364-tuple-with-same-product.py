class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        multiples = defaultdict(int)

        for i in range(n):
            for j in range(i + 1, n):
                multiples[nums[i] * nums[j]] += 1

        ans = 0
        for val in multiples.values():
            ans += (val * (val - 1) // 2) * 8
        return ans
