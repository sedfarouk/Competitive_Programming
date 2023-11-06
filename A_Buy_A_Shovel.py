k, r = map(int, input().split())

ans = 1
cost = k
while True:
    if cost % 10==0 or (cost-((cost//10)*10)) - r==0:
        print(ans)
        break
    cost += k
    ans += 1
    
    
     
    
    
