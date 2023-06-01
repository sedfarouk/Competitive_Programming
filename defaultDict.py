from collections import defaultdict

n, m = map(int, input().split())

groupA = defaultdict(list)
for i in range(n):
    word = input().strip()
    groupA[word].append(i + 1)

for _ in range(m):
    word = input().strip()
    if word in groupA:
        indices = ' '.join(map(str, groupA[word]))
        print(indices)
    else:
        print(-1)
