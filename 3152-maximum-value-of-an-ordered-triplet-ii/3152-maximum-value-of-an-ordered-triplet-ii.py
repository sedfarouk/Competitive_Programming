class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        mx, mn = nums[:2]
        sub = mx - mn
        vals = [0, sub]

        for i in range(2, n):
            if nums[i] < mn:
                mn, mx = nums[i], max(mx, mn)
            elif nums[i] > mx:
                mx = mn = nums[i]
            sub = max(sub, mx - mn)
            vals.append(max(sub, vals[-1]))

        mx = 0
        ans = float("-inf")
        for i in range(n - 1, -1, -1):
            ans = max(ans, mx * vals[i])
            mx = max(mx, nums[i])
        return ans