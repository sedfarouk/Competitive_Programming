class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [[] for _ in range(numRows)]
        currIdx = 0
        d = 1

        if numRows == 1:
            return s

        for c in s:
            if (rows[0] and currIdx == 0) or currIdx == numRows - 1:
                d *= -1

            rows[currIdx].append(c)
            currIdx += d

        return "".join(c for row in rows for c in row)
            



