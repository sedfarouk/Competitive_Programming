class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2): # for O(log(min(n, m)))
            nums1, nums2 = nums2, nums1

        l1, l2 = len(nums1), len(nums2)
        l, r = 0, l1
        while l <= r:
            p1 = l + (r - l) // 2
            p2 = (l1 + l2 + 1) // 2 - p1

            max_left1 = float("-inf") if p1 == 0 else nums1[p1 - 1]
            min_right1 = float("inf") if p1 == l1 else nums1[p1]
            max_left2 = float("-inf") if p2 == 0 else nums2[p2 - 1]
            min_right2 = float("inf") if p2 == l2 else nums2[p2]

            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if (l1 + l2) % 2 == 0:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
                return max(max_left1, max_left2)

            elif max_left1 > min_right2:
                r = p1 - 1

            else:
                l = p1 + 1