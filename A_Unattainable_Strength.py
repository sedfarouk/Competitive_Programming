def solve():
    t = int(input())
    energies = list(map(int, input().split()))
    energies.sort()
    smallest = 1
    
    for energy in energies:
        if energy <= smallest:
            smallest += energy
        else:
            break
    
    return smallest

print(solve())


