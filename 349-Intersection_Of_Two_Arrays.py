class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashset = set(nums1)
        unique = set()

        for num in nums2:
            if num in hashset:
                unique.add(num)

        return unique
