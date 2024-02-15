def solve():
    x = int(input())
    
    x_bin = bin(x)[:1:-1]
    k = x_bin.index('1')
    y = 1<<k
    
    if x!=y:
        return y
    if '0' not in x_bin:
        return y | 1 << len(x_bin)
    z_th = x_bin.index('0')
    return y | 1 << z_th
        
for _ in range(int(input())):
    print(solve())
