n = int(input())
lst= list(map(int, input().split()))

lst.sort() 

max_size = 0
left = 0
right = 0

while left < n:
    while right < n and lst[right] - lst[left] <= 5:
        right += 1
    max_size = max(max_size, right - left)
    left += 1

print(max_size)
