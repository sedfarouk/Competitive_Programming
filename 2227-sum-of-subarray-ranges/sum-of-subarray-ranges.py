class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)

        def smallerMonotonicStack(start, end, step):
            stk = []
            smaller = [(n if step == 1 else -1) for _ in range(n)]

            for i in range(start, end, step):
                while stk and (nums[stk[-1]] >= nums[i] if step == 1 else nums[stk[-1]] > nums[i]):
                    smaller[stk.pop()] = i
                stk.append(i)

            return smaller

        def greaterMonotonicStack(start, end, step):
            stk = []
            greater = [(n if step == 1 else -1) for _ in range(n)]

            for i in range(start, end, step):
                while stk and (nums[stk[-1]] <= nums[i] if step == 1 else nums[stk[-1]] < nums[i]):
                    greater[stk.pop()] = i
                stk.append(i)

            return greater

        nextSmaller, prevSmaller = smallerMonotonicStack(0, n, 1), smallerMonotonicStack(n - 1, -1, -1)
        nextGreater, prevGreater = greaterMonotonicStack(0, n, 1), greaterMonotonicStack(n - 1, -1, -1)

        ans = 0
        for i in range(n):
            ans += nums[i] * ((nextGreater[i] - i) * (i - prevGreater[i]))
            ans -= nums[i] * ((nextSmaller[i] - i) * (i - prevSmaller[i]))

        return ans

        
