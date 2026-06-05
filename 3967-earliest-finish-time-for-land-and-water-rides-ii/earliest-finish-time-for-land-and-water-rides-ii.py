class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n, m = len(landStartTime), len(waterStartTime)
        bestLand, bestWater = [float("inf")] * (n + 1), [float("inf")] * (m + 1)
        minLand, minWater = [float("inf")] * (n + 1), [float("inf")] * (m + 1)

        land, water = sorted(zip(landStartTime, landDuration)), sorted(zip(waterStartTime, waterDuration))
        landStartTime, landDuration = zip(*land)
        waterStartTime, waterDuration = zip(*water)

        for i in range(n - 1, -1, -1):
            bestLand[i] = min(landStartTime[i] + landDuration[i], bestLand[i + 1])
        
        for i in range(1, n + 1):
            minLand[i] = min(landDuration[i - 1], minLand[i - 1])

        for i in range(m - 1, -1, -1):
            bestWater[i] = min(waterStartTime[i] + waterDuration[i], bestWater[i + 1])

        for i in range(1, m + 1):
            minWater[i] = min(waterDuration[i - 1], minWater[i - 1])

        res = float("inf")
        for i in range(n):
            x = landStartTime[i] + landDuration[i]
            j = bisect_left(waterStartTime, x)
            res = min(res, bestWater[j], x + minWater[j])

        for i in range(m):
            x = waterStartTime[i] + waterDuration[i]
            j = bisect_left(landStartTime, x)
            res = min(res, bestLand[j], x + minLand[j])

        return res