from collections import defaultdict

def solve():
    s = input()
    hashmap = defaultdict(int)
    ans=""
    
    for i in s:
        hashmap[i]+=1
    
    cnt=0
    for key, val in hashmap.items():
        if val==2:
            cnt+=1
            ans+=key*2
    if cnt > 1:
        for key, val in hashmap.items():
            if val==1:
                ans+=key
    else:
        return s
            
    return ans
    
for _ in range(int(input())):
    print(solve())