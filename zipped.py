# Enter your code here. Read input from STDIN. Print output to STDOUT

marks, num_of_students = tuple(map(int,input().split()))

total_marks = []
for _ in range(num_of_students):
    marks = list(map(float, input().split()))
    total_marks.append(marks)
    
averages = [sum(marks)/num_of_students for marks in zip(*total_marks)]
    
for average in averages:
    print(average)
    
    

    
    
        