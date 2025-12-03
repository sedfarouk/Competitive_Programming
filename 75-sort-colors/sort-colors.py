class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        def arrange(st, num):
            while st < n and nums[st] == num:
                st += 1

            slow, fast = st, st + 1
            while fast < n:
                if nums[fast] == num:
                    nums[slow], nums[fast] = nums[fast], nums[slow]
                    slow += 1
                fast += 1

            return slow

        st2 = arrange(0, 0)
        st3 = arrange(st2, 1) 