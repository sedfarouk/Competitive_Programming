class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        mid = -1

        def binarySearch(l, r):
            while l <= r:
                m = l + (r - l) // 2

                if nums[m] == target: return m
                elif nums[m] < target: l = m + 1
                else: r = m - 1
            
            return -1

        while l <= r:
            m = l + (r - l) // 2

            if m < n - 1 and nums[m] > nums[m + 1]:
                mid = m
                break
            
            elif nums[m] > nums[-1]:
                l = m + 1

            else:
                r = m - 1

        return max(binarySearch(0, mid), binarySearch(mid + 1, n - 1))


        