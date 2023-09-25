"""Implement a function called sort students thai takes a list of student objects as input and sorts the list based on their CGPA (cumulative grade point avarage) in descending order.
Each studenst object has the following attributes: name(string) rollnumber(string) and cgpa (float). 
Test the function with difference input lists of students"""


class student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(studentlist):
  sorted_student = sorted(studentlist,
                          key=lambda student: student.cgpa,
                          reverse=True)
  return sorted_student


students = [
    student("John", "A001", 7.5),
    student("Jenna", "A002", 9.5),
    student("Jack", "A003", 6.3),
]

sorted_student = sort_students(students)
for student in sorted_student:
  print("Name : {}, Roll number : {}, CGPA : {}.".format(
      student.name, student.roll_number, student.cgpa))
