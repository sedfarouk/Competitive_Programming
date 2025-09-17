class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [[] for _ in range(numRows)]
        n = len(s)
        ptr = 0

        # while ptr < n:
        #     for i in range(ptr, min(ptr + numRows, n)):
        #         rows[i - ptr].append(s[i])
            
        #     ptr += numRows
        #     for i in range(numRows - 2, 0, -1):
        #         if ptr >= len(s):
        #             break
        #         rows[i].append(s[ptr])
        #         ptr += 1

        # return "".join(["".join(row) for row in rows])


        # SHORTER & SMARTER - Go down with 1, go up with -1
        if numRows == 1 or numRows >= len(s):
            return s

        d = 1
        for i in range(n):
            rows[ptr].append(s[i])

            if ptr == 0:
                d = 1
            elif ptr == numRows - 1:
                d = -1
            ptr += d

        return "".join(["".join(row) for row in rows]) 

