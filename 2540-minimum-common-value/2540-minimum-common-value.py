class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        cnt1, cnt2 = set(nums1), set(nums2)
        
        intersection = cnt1.intersection(cnt2)
        if not intersection:
            return -1
        return min(intersection)
#         nums1.sort()
#         nums2.sort()

#         nums1_ptr, nums2_ptr = 0, 0

#         while nums1_ptr < len(nums1) and nums2_ptr < len(nums2):
#             if nums1[nums1_ptr]==nums2[nums2_ptr]:
#                 return nums1[nums1_ptr]
#             if nums1[nums1_ptr] > nums2[nums2_ptr]:
#                 nums2_ptr+=1
#             else:
#                 nums1_ptr+=1
#         return -1