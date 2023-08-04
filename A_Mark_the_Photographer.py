def solve():
    n, min_diff = map(int, input().split())
    people = list(map(int, input().split()))
    people.sort()
    front_row = people[:n]
    back_row = people[n:]
    
    for i in range(n):
        if back_row[i]-front_row[i] < min_diff:
            return "NO"
        
    return "YES"
    
for _ in range(int(input())):
    print(solve())