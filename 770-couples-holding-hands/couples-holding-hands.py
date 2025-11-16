class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        def backtrack(idx):
            for i in range(idx, len(row), 2):
                x, y = row[i], row[i + 1]
                px, py = i, i + 1
                if x > y: 
                    x, y = y, x
                    px, py = py, px

                if y - x != 1 or x % 2:
                    ix = row.index(x + (-1 if x % 2 else 1))
                    row[ix], row[py] = row[py], row[ix]
                    ans = backtrack(i + 2) + 1
                    row[ix], row[py] = row[py], row[ix]

                    return ans
            return 0

        return backtrack(0)