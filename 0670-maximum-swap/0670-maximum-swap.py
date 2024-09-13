class Solution:
    def maximumSwap(self, num: int) -> int:
        ans = num
        num = [i for i in str(num)]

        for i in range(len(num)):
            for j in range(i+1, len(num)):
                x = num[:]
                x[i], x[j] = x[j], x[i]
                ans = max(ans, int("".join(x)))
        return ans
        