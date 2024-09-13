class Solution:
    def maximumSwap(self, num: int) -> int:
        num = [i for i in str(num)]
        maxx = st = 0

        for i in range(1, len(num)):
            if num[i] > num[i-1]:
                st = i
                break

        for i in range(st, len(num)):
            digit = int(num[i])
            if digit >= maxx:
                maxx = digit
                st = i

        i = 0
        while int(num[i]) >= maxx and i < st:
            i += 1
        num[i], num[st] = num[st], num[i]
        return int("".join(num))

        # ans = num
        # num = [i for i in str(num)]

        # for i in range(len(num)):
        #     for j in range(i+1, len(num)):
        #         x = num[:]
        #         x[i], x[j] = x[j], x[i]
        #         ans = max(ans, int("".join(x)))
        # return ans
        