# Enter your code here. Read input from STDIN. Print output to STDOUT
def isSuper(setA, subset):
    if set_A.issuperset(subset):
        return True
    return False

set_A = set(map(int, input().split()))

for _ in range(int(input())):
    subset = set(map(int, input().split()))
    if isSuper(set_A, subset)==False:
        print(False)
        break
    else:
        continue


    