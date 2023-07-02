# Codeforces - A2SV Contest

def func(a, b):
    for i in range(a-1):
        for j in range(b):
            if grid[i][j]=='*' and grid[i+1][j]=='.':
                grid[i][j]='.'
                grid[i+1][j]='*'

for _ in range(int(input())):
    a, b = map(int, input().split())
    
    grid = []
    for i in range(a):
        row = list(input())
        grid.append(row)
    for j in range(a):
        func(a,b)
                
    for j in range(len(grid)):
        print(''.join(grid[j]))
    print()