class Solution:
    def maxPower(self, stations: List[int], rd: int, k: int) -> int:
        n = len(stations)
        diff = [0] * n
        
        for idx, station in enumerate(stations):
            diff[max(0, idx - rd)] += station
            if idx + rd + 1 < n: diff[idx + rd + 1] -= station

        for i in range(n):
            if i > 0: diff[i] += diff[i - 1]
            stations[i] = diff[i]

        def f(x):
            q = k
            d = [0] * n
            for i in range(n):
                if i > 0: d[i] += d[i - 1]

                if stations[i] + d[i] < x:
                    y = x - (stations[i] + d[i])

                    if y > q:
                        return False
                    
                    d[i] += y; q -= y
                    if i + 2 * rd + 1 < n: d[i + 2 * rd + 1] -= y

            return True

        l, r = min(stations), max(stations) + k
        ans = l
        while l <= r:
            m = l + (r - l) // 2

            if f(m):
                ans = m
                l = m + 1
            else:
                r = m - 1

        return ans
            

        