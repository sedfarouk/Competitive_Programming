class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        n = len(points)

        def calcDist(x, y):
            return (x[0]-y[0])**2 + (x[1]-y[1])**2

        for i in range(n):
            h = defaultdict(int)

            for j in range(n):
                dist = calcDist(points[i], points[j]) 
                h[dist] += 1

            for val in h.values():
                ans += val * (val - 1)
        return ans
