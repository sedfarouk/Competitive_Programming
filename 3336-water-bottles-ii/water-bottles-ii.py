class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        exchangeBottles = 0

        while numBottles >= numExchange:
            numBottles -= numExchange
            exchangeBottles += 1; numExchange += 1
            
            if numExchange > numBottles:
                ans += exchangeBottles
                numBottles += exchangeBottles
                exchangeBottles = 0

        return ans
        