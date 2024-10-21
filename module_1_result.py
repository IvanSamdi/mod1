grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny:', 'Bilbo:', 'Steve:', 'Khendrik:', 'Aaron:'}
A = sum(grades[0]) / len(grades[0])
B = sum(grades[1]) / len(grades[1])
J = sum(grades[2]) / len(grades[2])
K = sum(grades[3]) / len(grades[3])
S = sum(grades[4]) / len(grades[4])
grades = [A, B, J, K, S]
list_students = list(students)
list_students = sorted(list_students)
average_grade = dict(zip(list_students, grades))
print(average_grade)
