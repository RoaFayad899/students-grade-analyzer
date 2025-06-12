#Determining of the students' number and Collecting Data
num_students = int (input ("Please enter the number of students:"))

students_names = []
students_grades = []

for i in range(num_students):
    name = input (f"Name of Student {i+1}:")
    grade = float (input(f"Grade of Student {i+1} {name} (It must be between 0 and 100):"))
    if grade < 0 or grade > 100:
        grade = float (input(f"Grades must be between 0 and 100! Re enter Grade of Student {i+1} {name}: "))
    
    students_names.append(name)
    students_grades.append(grade)





