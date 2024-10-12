class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = r = 0
        while l < m and r < n:
            if nums1[l] > nums2[r]:
                prev = nums1[l]
                for i in range(l+1, len(nums1)):
                    temp = prev
                    prev = nums1[i]
                    nums1[i] = temp
                nums1[l] = nums2[r]
                m += 1; r += 1; l += 1
            else:
                l += 1

        while r < n:
            nums1[l] = nums2[r]
            r += 1; l += 1
        