class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # APPROACH 1
        slow = fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow==fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

        # APPROACH 2
        # bit_manip = 0
        # for num in nums:
        #     if (bit_manip&(1<<num))!=0:
        #         return num
        #     bit_manip |= (1<<num)

        # APPROACH 3
        # i = 0
        # n = len(nums)
        
        # while i < n:
        #     correctIdx = nums[i]
        #     if nums[i] != nums[correctIdx-1]:
        #         nums[i], nums[correctIdx-1] = nums[correctIdx-1], nums[i]
                
        #     else:
        #         i += 1
                
        # for j in range(n):
        #     if j != nums[j]-1:
        #         return nums[j]
