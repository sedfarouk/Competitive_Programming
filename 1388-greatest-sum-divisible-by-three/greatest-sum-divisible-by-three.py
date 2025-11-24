class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        summ = sum(nums)
        h1, h2 = [], []

        if summ % 3 == 0: return summ

        for num in nums:
            if num % 3 == 1 and (len(h1) < 2 or -h1[0] > num):
                if len(h1) == 2 and -h1[0] > num: heappop(h1)
                heappush(h1, -num)

            elif num % 3 == 2 and (len(h2) < 2 or -h2[0] > num):
                if len(h2) == 2 and -h2[0] > num: heappop(h2)
                heappush(h2, -num)

        sub = summ
        if summ % 3 == 1:
            if h1: sub = -max(h1)
            if len(h2) == 2: sub = min(sub, -sum(h2))
        else:
            if h2: sub = -max(h2)
            if len(h1) == 2: sub = min(sub, -sum(h1))

        return summ - sub
