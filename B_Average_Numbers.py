# Codeforces - A2SV Contest

t = int(input())

lst = list(map(int, input().split()))

mean = sum(lst)/len(lst)
cnt = 0

for i in range(len(lst)):
    if lst[i]==mean:
        cnt+=1
print(cnt)

for i in range(len(lst)):
    if lst[i]==mean:
        print(i+1, end=" ")
