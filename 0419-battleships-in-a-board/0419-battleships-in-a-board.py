class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        
        def dfs(r, c):
            if r<0 or c<0 or r==m or c==n or board[r][c]==".":
                return
            
            board[r][c]="."
            for x, y in dirs:
                dfs(r+x, c+y)
                
        ans = 0    
        for i in range(m):
            for j in range(n):
                if board[i][j]=='X':
                    dfs(i, j)
                    ans += 1
                    
        return ans
                
            
        