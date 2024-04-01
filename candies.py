def solve():
    n = int(input())

    if n%2==0: return [-1]
    
    ans = []    
    while n > 1:
        y = n%2
        n //= 2
        if n%2==0:
            n += 1
            ans.append(1)
        else:
            ans.append(2)
        
    return ans[::-1]

for _ in range(int(input())):
    res = solve()
    if res==[-1]: print(-1)
    else:
        print(len(res))
        print(*res)
                    
            
