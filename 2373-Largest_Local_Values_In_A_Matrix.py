# LeetCode - 2373

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans, final = [], []
        for i in range(len(grid)-2):
            rows = grid[i:i+3]
            for j in range(len(grid)-2):
                max_num = float('-inf')
                for k in rows:
                    max_row = max(k[j:j+3])
                    max_num = max(max_row, max_num)
                ans.append(max_num)
        l = len(grid)-2
        for i in range(0,len(ans),l):
            final.append(ans[i:i+l])
        return final   
