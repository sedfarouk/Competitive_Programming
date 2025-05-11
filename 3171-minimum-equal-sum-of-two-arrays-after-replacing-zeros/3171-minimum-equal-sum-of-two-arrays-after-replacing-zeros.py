class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        z1, z2 = nums1.count(0), nums2.count(0)
        s1, s2 = sum(nums1), sum(nums2)

        if z1 == 0 and z2 == 0: return s1 if s1 == s2 else -1
        if (z1 == 0 and s1 < s2 + z2) or (z2 == 0 and s2 < s1 + z1): return -1

        def f(x):
            return s1 + z1 <= x and s2 + z2 <= x

        l, r = 0, 10**12
        ans = -1
        while l <= r:
            m = l + (r - l) // 2

            if f(m):
                r = m - 1
                ans = m

            else:
                l = m + 1
        
        return ans

