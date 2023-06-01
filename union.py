# Enter your code here. Read input from STDIN. Print output to STDOUT# Enter your code here. Read input from STDIN. Print output to STDOUT

num_of_English = int(input())
students_English = set(map(int, input().split()))
num_of_French = int(input())
students_French = set(map(int, input().split()))

print(len(students_English.union(students_French)))