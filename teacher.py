 #
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

    # Get the assignments where student is not recorded
    def update_missing_assignments(self,student):
        for assignment in self.assignment_list:
            if student not in assignment.get_assignments():
                self.update_assignment(assignment,student)
    # Remove Student from roster and pass name to remove from assignment
    def remove_student_from_roster(self, student_name):
        self.class_roster.remove(student_name)
        return student_name
    # Remove Student from each of his assignments
    def remove_student_assingments(self,student_name):
        for assignment in self.assignment_list:
            assignment.remove_student(student_name)
            print("removed {} from {}".format(assignment.pop(student_name, None),assignment))
    
    # Adding assignment to the list and to each student
    def add_assignment(self, assignment_entry):
        new_assignment = Assignment(assignment_entry)
        self.assignment_list.append(new_assignment)
        return new_assignment
    # Adding a grade for the assignment
    def add_grade_to_student(self,assignment,student, grade):
        assignment.set_grade(student,grade)
        print("Added {} to {}".format(grade, student))

    # Add grades to students added after the assignment
    def update_assignment(self, assignment, student):
        grade = int(input("What grade did {} get on {}:".format(student,assignment.get_name())))
        if(grade >= 0 and grade <=100):
            assignment.set_grade(student, grade)

    # Change the grade of assignment for student
    def edit_grade(assignment,edit_student,new_grade):
        assignment_list[assignment].set_grade(edit_student,new_grade)

    # Returns if the Teacher has any assignments
    def has_assignments(self):
        return len(self.assignment_list) > 0

    # Get the class roster     
    def get_roster(self):
        return self.class_roster 

    # Print/Return all of the grades for the assigment
    def get_assignment(self,assignment):
        if assignment in self.get_assignments():
            return self.get_assignments()[assignment]

    def get_assignments(self):
        return self.assignment_list

    def view_assignments(self):
        for assignment in self.get_assignments():
            print("{}: {}".format(assignment.get_name(),assignment.get_grades()))

    # Return student grade and assignmentname.
    def view_assignments_by_student(self, student_name):
        student_assignemnts = {}
        for assignment in self.get_assignments():
            student_assignemnts[assignment.get_name] = assignment.get_grade(student_name)
            print("{}: {}".format(assignment.get_grade(student_name), assignment.get_name()))
        input()



    #def grade_by_student(self,student_name):
        #for assignments in self.get_ass
    def get_assignment(self,assignment_name):
        print(self.assignment_list[assignment_name].get_grades())
