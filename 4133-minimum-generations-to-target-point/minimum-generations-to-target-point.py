class Solution:
    def minGenerations(self, points: List[List[int]], target: List[int]) -> int:
        points = set(tuple(p) for p in points)
        target = tuple(target)

        if target in points:
            return 0

        ans = 0

        while True:
            current = list(points)
            new_points = set()

            for i in range(len(current)):
                for j in range(i, len(current)):
                    a = current[i]
                    b = current[j]

                    new = (
                        (a[0] + b[0]) // 2,
                        (a[1] + b[1]) // 2,
                        (a[2] + b[2]) // 2,
                    )

                    if new == target:
                        return ans + 1

                    if new not in points:
                        new_points.add(new)

            if not new_points:
                return -1

            points |= new_points
            ans += 1