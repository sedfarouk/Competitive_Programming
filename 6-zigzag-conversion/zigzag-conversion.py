class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [[] for _ in range(numRows)]
        currRow = 0
        direction = -1

        if numRows == 1: return s

        for i in range(len(s)):
            if currRow == 0 or currRow == numRows - 1:
                direction *= -1

            rows[currRow].append(s[i])
            currRow += direction

        ans = "".join(["".join(row) for row in rows])
        return ans