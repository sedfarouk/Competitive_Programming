class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        slow = 0

        for fast in range(n):
            while slow < fast and nums[slow] != val:
                slow += 1
            nums[slow], nums[fast] = nums[fast], nums[slow]
        
        for i in range(n):
            if nums[i] == val:
                return i
        return n
             