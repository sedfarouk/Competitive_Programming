# Leetcode 840 

def check_diagonals(matrix):
    n = int(len(matrix)/2)+1
    front, back = [], []
    for i in range(n):
        for j in range(n):
            if i==j:
                front.extend([matrix[i][j],matrix[n-i][n-j]])
                back.extend([matrix[i][n-j],matrix[n-j][i]])
    if sum(front[:len(matrix)]) == sum(back[:len(matrix)]):
        return True
    return False

def check_rows(matrix):
    top_row, middle_row, bottom_row = sum(matrix[0]), sum(matrix[1]), sum(matrix[2])
    if top_row==middle_row==bottom_row:
        return True
    return False
    
def check_cols(matrix):
    right_col, middle_col, left_col = 0, 0, 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            right_col+=matrix[i][0]
            middle_col+=matrix[i][1]
            left_col+=matrix[i][2]
            
    if right_col==middle_col==left_col:
        return True
    return False

def check_matrix(matrix):
    nums = set()
    for i in matrix:
        for j in range(len(i)):
            if i[j]<10 and i[j]>0:
                nums.add(i[j])
    if len(nums)!= 9:
        return False
    return True

def numMagicSquaresInside(grid: list[list[int]]):  
    ans = 0
    for i in range(len(grid)-2):
        for j in range(len(grid[0])-2):
            sub_grid = grid[i:i+3]
            for k in range(len(sub_grid)):
                sub_grid[k] = sub_grid[k][j:j+3]
            print(sub_grid)
            if check_matrix(sub_grid) is False:
                continue
            else:
                if check_diagonals(sub_grid) and check_cols(sub_grid) and check_rows(sub_grid):
                    ans+=1
    return ans
nums = [[3,2,9,2,7],[6,1,8,4,2],[7,5,3,2,7],[2,9,4,9,6],[4,3,8,2,5]]
print(numMagicSquaresInside(nums))
