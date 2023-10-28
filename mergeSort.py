# Leetcode 912 - Sort An Array

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums

        mid = len(nums) // 2
        nums1 = self.sortArray(nums[mid:])
        nums2 = self.sortArray(nums[:mid])

        return self.merge(nums1, nums2)               
    
    def merge(self, arr1, arr2):
        sorted_arr = []
        i = j = 0

        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                sorted_arr.append(arr1[i])
                i += 1
            else:
                sorted_arr.append(arr2[j])
                j += 1

        while i < len(arr1):
            sorted_arr.append(arr1[i])
            i += 1

        while j < len(arr2):
            sorted_arr.append(arr2[j])
            j += 1

        return sorted_arr
        
