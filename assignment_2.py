#Functions
def display_student_summary (names_list, grades_list):
    print("The Summary of Grades in this Class")
    for i in range (len(names_list)):
        print(names_list[i], ":", grades_list[i])

def get_avg_grade (grades_list):
    sum = 0
    for i, elet in enumerate(grades_list):
        sum += elet
    return sum / len(grades_list)  

def get_heighest_grade (names_list, grades_list):
    max = 0
    for i, elet in enumerate(grades_list):
        if elet >= max:
            max = elet
    print ("The highest grade was", max,". It was given to:")
    for i, elet in enumerate(grades_list):
        if elet == max:
            print(names_list[i])
    return max

def count_passed(grades_list):
    count = 0
    for i, elet in enumerate(grades_list):
        if elet >= 60:
            count += 1
    return count

    
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


#Calling Functions to determine
#The summary of grades in this class
display_student_summary(students_names, students_grades)

#The average of the grades
print ("The average of grades in this class is:", get_avg_grade(students_grades))

#The highest grade in the class
get_heighest_grade(students_names, students_grades)

#The count of students who passed
print("The number of students who passed is:", count_passed(students_grades))



