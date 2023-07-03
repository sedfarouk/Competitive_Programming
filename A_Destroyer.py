# Codeforces - A2SV Contest

def solve():
    t = int(input())
    arr = list(map(int, input().split()))
    cnt = [0] * (max(arr)+1)
    for i in arr:
        cnt[i]+=1
    
    for i in range(len(cnt)-1):
        if cnt[i] >= cnt[i+1] and cnt[i]-cnt[i+1] >= 0 or cnt[i]-sum(set(cnt[i+1:])) == cnt[i]:
            continue
        else:
            return "NO"
    return "YES"          
    
for _ in range(int(input())):
    print(solve())