class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(l, r):
            if l == r:
                return [nums[l]]

            m = l + (r - l) // 2
            left = mergeSort(l, m)
            right = mergeSort(m + 1, r)

            return merge(left, right)

        def merge(arr1, arr2):
            p1 = p2 = 0
            sorted_arr = []

            while p1 < len(arr1) and p2 < len(arr2):
                if arr1[p1] < arr2[p2]:
                    sorted_arr.append(arr1[p1])
                    p1 += 1
                else:
                    sorted_arr.append(arr2[p2])
                    p2 += 1

            sorted_arr.extend(arr1[p1:])
            sorted_arr.extend(arr2[p2:])

            return sorted_arr

        return mergeSort(0, len(nums) - 1)
