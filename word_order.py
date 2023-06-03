unique = {}
for _ in range(int(input())):
    word = str(input())
    if word in unique:
        unique[word]+=1
    else:
        unique[word] = 1

print(len(unique))
print(*unique.values())