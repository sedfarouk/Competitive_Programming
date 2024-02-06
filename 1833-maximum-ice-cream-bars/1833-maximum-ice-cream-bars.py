class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        maxx = max(costs)
        cnt = [0]*(maxx+1)

        for cost in costs:
            cnt[cost] += 1

        ans = 0
        i = 1
        while coins >= i and i < len(cnt):
            if cnt[i] > 0:
                num = min(cnt[i]*i, (coins//i)*i)
                ans += num // i
                coins -= num
            i += 1

        return ans


        