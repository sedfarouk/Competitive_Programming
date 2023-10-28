class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums

        mid = len(nums) // 2
        nums1 = self.sortArray(nums[mid:])
        nums2 = self.sortArray(nums[:mid])

        sorted_nums = merge(nums1, nums2)

        return sorted_nums                
    
    def merge(self, arr1, arr2):
        sorted_arr = []
        i = j = 0

        while i < len(arr1) and j < len(arr):
            if arr[i] < arr[j]:
                sorted_arr.append(arr[i])
                i += 1
            else:
                sorted_arr.append(arr[j])
                j += 1

        sorted_arr.extend(arr[i:])
        sorted_arr.extend(arr[j:])
        
        return sorted_arr
        