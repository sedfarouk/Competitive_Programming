# Codeforces Contest

for _ in range(int(input())):
    input()
    board = []
    for i in range(8):
        curr_line = input()
        board.append(curr_line)
        
    for i in range(1,len(board)-1):
        for j in range(1,len(board)-1):
            if board[i][j]=='#' and board[i-1][j-1]=='#' and board[i+1][j+1]=='#' and board[i+1][j-1]=='#' and board[i-1][j+1]=='#':
                print(i+1,j+1)
                
        
