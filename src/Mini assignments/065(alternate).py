#############################################################################
#Author: Mohammad El-Hassan
#Description: Mini Assingment #65 (alternate)
#Date Created: 11/12/2022
#Date Modified: 11/12/2022
#############################################################################

class_grade = {}
student_grade = input("Enter your marks ")
student_grade = student_grade.split(" ")
course_index = 0
mark_index = 1
for i in range(4):
    class_grade[student_grade[course_index]] = int(student_grade[mark_index])
    course_index += 2
    mark_index += 2
print(class_grade)
