class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        monostack = deque()
        next_greater = [-1] * n

        for _ in range(2):
            for i in range(n):
                while monostack and nums[monostack[-1]] < nums[i]:
                    next = monostack.pop()
                    next_greater[next] = nums[i]              
                monostack.append(i)

        return next_greater