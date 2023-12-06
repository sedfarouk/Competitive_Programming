class Solution:
    def totalMoney(self, n: int) -> int:
        x = n//7
        ans = 0

        for i in range(1, x+1):
            ans += sum(range(i, i+7))

        r = n % 7
        ans += sum(range(x+1, r+x+1))
        return ans
        