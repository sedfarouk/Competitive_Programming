class Solution:
    def maximumMEX(self, nums: List[int]) -> List[int]:
        n = len(nums)
        digits = defaultdict(lambda: deque())

        for i in range(n):
            digits[nums[i]].append(i)

        res = []
        st = idx = curr = 0

        while idx < n:
            while digits[curr] and digits[curr][0] < st:
                digits[curr].popleft()
            if digits[curr]:
                idx = max(idx, digits[curr].popleft())
                curr += 1
            else:
                res.append(curr)
                idx += 1; st = idx; curr = 0
                
        return res
            
            
                