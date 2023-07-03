# 36. Leetcode - Medium

class Solution:
    def check_9_by_9(self, arr:list[list[int]], i:int): 
        columns = list(map(list, zip(*arr)))      
        rows, cols = [], []
        for j in arr[i]:  
            if j not in rows:
                if j!='.':
                    rows.append(j)
            else:
                return False
        
        for j in columns[i]:  
            if j not in cols:
                if j!='.':
                    cols.append(j)
            else:
                return False
        
    def check_3_by_3(self,arr:list[list[int]]):      
        rows_cols = []
        for j in arr:  
            for k in j:
                if k not in rows_cols:
                    if k!='.':
                        rows_cols.append(k)
                else:
                    return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if self.check_9_by_9(board, i) is False:
                return False
        for i in range(0,9,3):
            for j in range(0,9,3):
                subgr = []
                for k in board[i:i+3]:
                    subgr.append(k[j:j+3])  
                if self.check_3_by_3(subgr) is False:
                    return False
        return True    
        
