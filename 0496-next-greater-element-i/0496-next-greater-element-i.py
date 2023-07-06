class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            for j in range(len(nums2)):
                if i==nums2[j]:
                    if max(nums2[j:])!=i:
                        for k in range(j,len(nums2)):
                            if nums2[k] > nums2[j]:
                                ans.append(nums2[k])
                                break
                    else:
                        ans.append(-1)
        return ans
