class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0

        for i in range(1, len(points)):
            x = abs(points[i][0]-points[i-1][0])
            y = abs(points[i][1]-points[i-1][1])

            if x < y:
                ans += x + abs(points[i][1]-points[i-1][1])-x
            elif x > y:
                ans += y + abs(points[i][0]-points[i-1][0])-y
            else:
                ans += x
        return ans

        