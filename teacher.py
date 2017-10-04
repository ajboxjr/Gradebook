from assignment import *
from student import *
class Teacher:
    def __init__(self,name):
        self.name = name
        self.class_roster = []
        self.assignment_list = []
    
    # Add student to the class roster
    def add_student_to_roster(self,student):
        self.class_roster.append(student)
        print("added {} to the roster".format(student))
    # Remove Student from roster and pass name to remove from assignment
    def remove_student_from_roster(self, student_name):
        self.class_roster.remove(student_name)
        self.remove_student_assignments(student_name)
    def remove_student_assingments(self,student_name):
        for assignment in self.assignment_list:
            assignment.pop(student_name, None)
            print("removed {} from {}".format(assignment.pop(student_name, None),assignment)
        
    # Adding assignment to the list and to each student
    def add_assignment(self, assignment_entry):
        new_assignment = Assignment(assignment_entry)
        self.assignment_list.append(new_assignment)
        for student  in self.get_roster():
            grade = int(input("What grade did {} get on {}".format(student, assignment_entry)))
            new_assignment.add_grades_to_student(student,grade)
    
    # Get the class roster     
    def get_roster(self):
        return self.class_roster 

    def view_assignment(self,asgnt_name):
        if asgnt_name in self.assignment_list:
            print(asgnt_name)
