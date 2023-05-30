if __name__ == '__main__':
    class_grades = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        class_grades.append([name,score])
    
class_grades.sort(key=lambda x:x[1], reverse=True)

lowest_grade = class_grades[-1][1]
for i in class_grades:
    if i[1]==lowest_grade:
        class_grades.remove(i)

second_max_students = []
lowest2_grade = class_grades[-1][1]
for i in class_grades:
    if i[1]==lowest2_grade:
        second_max_students.append(i)
    
second_max_students.sort(key=lambda x:x[0])      
for i in second_max_students:
    print(i[0])