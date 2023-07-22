def transpose(mat):
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

def solve():
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))
    mat = [lst1, lst2]
    
    if (mat[0][0] < mat[0][1] and mat[0][0]<mat[1][0]) and (mat[1][1] > mat[1][0] and mat[1][1] > mat[0][1]):
        return "YES"

    for i in range(4):
        mat = transpose(mat)
        for j in range(2):
            mat[j][0], mat[j][1] = mat[j][1], mat[j][0]
        
        if (mat[0][0] < mat[0][1] and mat[0][0]<mat[1][0]) and (mat[1][1] > mat[1][0] and mat[1][1] > mat[0][1]):
            return "YES"
    return "NO"

for _ in range(int(input())):
    print(solve())