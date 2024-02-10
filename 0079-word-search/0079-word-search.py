class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        def dfs(r, c, i):
            if i==len(word):
                return True

            if r<0 or c<0 or r==len(board) or c==len(board[0]) or board[r][c]!=word[i] or (r, c) in visited:
                return False

            visited.add((r, c))
            res = False
            for x, y in dirs:
                res = res or dfs(r+x, c+y, i+1)
            visited.remove((r, c))
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False
        
            

            

            

            

            
        