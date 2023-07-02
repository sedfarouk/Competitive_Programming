# Codeforces - A2SV Contest

for i in range(int(input())):
    n1, n2 = map(int, input().split())
    if (n1%2==0) or (n1-n2)%2==0:
        print("YES")
    else:
        print("NO")

