for _ in range(int(input())):
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    
    if (x1 == x2 and y1 + y2 == x1) or (x1 == y2 and y1 + x2 == x1) or (y1 == x2 and x1 + y2 == y1) or (y1 == y2 and x1 + x2 == y1):
        print("Yes")
    else:
        print("No")
