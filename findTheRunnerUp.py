if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

maxNum = max(arr)
arr.sort(key=lambda x:(x<maxNum,x), reverse=True)
print(arr[0])

