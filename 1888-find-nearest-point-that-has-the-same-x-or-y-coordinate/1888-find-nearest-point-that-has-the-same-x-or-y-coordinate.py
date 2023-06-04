class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_dist, ans = float("inf"), -1
        for i, (a, b) in enumerate(points):
            if a == x or b == y:
                man_dist = abs(a - x) + abs(b - y)
                if man_dist < min_dist:
                    ans, min_dist = i, man_dist
        return ans
