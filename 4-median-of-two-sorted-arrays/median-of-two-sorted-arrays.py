class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        l1, l2 = len(nums1), len(nums2)
        l, r = 0, len(nums1)
        while l <= r:
            ptr1 = l + (r - l) // 2
            ptr2 = (l1 + l2 + 1) // 2 - ptr1

            max_left1 = float("-inf") if ptr1 == 0 else nums1[ptr1 - 1]
            max_left2 = float("-inf") if ptr2 == 0 else nums2[ptr2 - 1]
            min_right1 = float("inf") if ptr1 == l1 else nums1[ptr1]
            min_right2 = float("inf") if ptr2 == l2 else nums2[ptr2]

            if min_right1 >= max_left2 and min_right2 >= max_left1:
                if (l1 + l2) % 2:
                    return max(max_left1, max_left2)
                
                return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2

            elif max_left1 > min_right2:
                r = ptr1 - 1
            
            else:
                l = ptr1 + 1

        