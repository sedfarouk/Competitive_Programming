class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles

        while numBottles >= numExchange:
            newBottles = numBottles // numExchange
            ans += newBottles
            numBottles -= newBottles * (numExchange - 1)

        return ans
        