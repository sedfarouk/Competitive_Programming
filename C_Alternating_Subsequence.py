def solve():
    t = int(input())
    sequence = list(map(int, input().split()))
        
    right = 0
    pos, neg = float("-inf"), float("-inf")
    ans = 0
    recent = sequence[0]
    
    while right < len(sequence):
        if recent < 0 and sequence[right] < 0:
            neg = max(neg, sequence[right])
        if recent > 0 and sequence[right] > 0:
            pos = max(pos, sequence[right])
        if recent < 0 and sequence[right] > 0:
            ans+=neg
            neg = float("-inf")
            pos = max(pos, sequence[right])
        if recent > 0 and sequence[right] < 0:
            ans+=pos
            pos = float("-inf")
            neg = max(neg, sequence[right])
        recent = sequence[right]
        right+=1
        
    if neg!=float("-inf"):
        ans+=neg
    if pos!=float("-inf"):
        ans+=pos
            
    return ans       

for _ in range(int(input())):
    print(solve())