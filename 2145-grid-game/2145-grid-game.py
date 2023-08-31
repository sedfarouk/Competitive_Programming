class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        top = [0]*(len(grid[0])+2)
        down = [0]*(len(grid[0])+2)

        # Prefix sum for bottom row
        for i in range(1, len(down)-1):
            down[i] = grid[1][i-1] + down[i-1]
        
        # Suffix sum for top row
        for i in range(len(top)-2, 0, -1):
            top[i] = grid[0][i-1] + top[i+1]
 
        res = []
        # Find best answers
        for i in range(1, len(top)-1):
            res.append(max(top[i+1], down[i-1]))
        # return minimum since second robot gets that
        return min(res)