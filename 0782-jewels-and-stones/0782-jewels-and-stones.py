class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set([i for i in jewels])
        ans = 0

        for letter in stones:
            if letter in jewels:
                ans += 1

        return ans
        