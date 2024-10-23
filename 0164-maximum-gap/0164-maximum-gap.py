class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        lo, hi, n = min(nums), max(nums), len(nums)
        if n <= 2: return hi - lo

        buckets = defaultdict(list)
        for num in nums:
            idx = n-2 if num==hi else (num - lo) * (n-1) // (hi - lo)
            buckets[idx].append(num)

        maxmins = [(min(buckets[i]), max(buckets[i])) for i in range(n-1) if buckets[i]]
        maxx = 0
        for i in range(1, len(maxmins)):
            mx, mn = maxmins[i-1][1], maxmins[i][0]
            maxx = max(maxx, mn-mx)
        return maxx