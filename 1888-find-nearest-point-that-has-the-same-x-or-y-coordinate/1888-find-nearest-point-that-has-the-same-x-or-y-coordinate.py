class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ans = {}
        for point in points:
            if point[0]==x or point[1]==y:
                ans[points.index(point)] = abs(x-point[0])+abs(y-point[1])
        for i,j in ans.items():
            if j==min(ans.values()):
                return i
        return -1
