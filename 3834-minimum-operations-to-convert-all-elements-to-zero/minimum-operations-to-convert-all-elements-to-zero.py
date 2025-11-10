class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        stk = []
        nextSmaller = [n] * n

        for i in range(n):
            while stk and nums[stk[-1]] > nums[i]:
                nextSmaller[stk.pop()] = i
            stk.append(i)

        indices = defaultdict(list)
        for i in range(n):
            if nums[i] > 0: indices[nums[i]].append(i)

        ans = 0
        for val in indices.values():
            cnt = 1
            for i in range(len(val) - 1):
                if nextSmaller[val[i]] < val[i + 1]:
                    cnt += 1

            ans += cnt

        return ans

        
