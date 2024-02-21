class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def recurse(row, col):
            if (row, col) in memo: return memo[(row, col)]
            
            if row==0 and col==0:
                return 1
            
            if row < 0 or col < 0:
                return 0

            memo[(row, col)] = recurse(row, col-1) + recurse(row-1, col)
            return memo[(row, col)]
        return recurse(m-1, n-1)

        
        