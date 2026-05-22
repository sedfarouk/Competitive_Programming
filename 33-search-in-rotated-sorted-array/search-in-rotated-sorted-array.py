class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def binarySearch(l, r):
            while l <= r:
                m = l + (r - l) // 2

                if nums[m] == target: return m
                elif nums[m] < target: l = m + 1
                else: r = m - 1
            
            return -1

        def findPivot(nums):
            l, r = 0, len(nums) - 1
            while l < r:
                m = (l + r) // 2
                if nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m
            return l

        pivot = findPivot(nums)

        return max(binarySearch(0, pivot - 1), binarySearch(pivot, n - 1))  


        