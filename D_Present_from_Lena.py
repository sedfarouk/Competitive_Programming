def solve():
    t = int(input())
    arr = []
    s = []
    for j in range(t+1):
        arr.append(' '*2*(t-j))
    for j in range(t):
        s.append(j)
    for j in range(t,-1,-1):
        s.append(j)
    for j in range(t+1):
        x = s[:j+1]
        x.extend(s[len(s)-j:])
        arr[j]+=' '.join(map(str,x))
    arr.extend(arr[len(arr)-2::-1])
    
    for i in arr:
        print(i)
        
solve()



    

    
    