from datetime import *

'''
The Gradebook contains

'''

class Gradebook(object):
    def __init__(self):
        self.class_roster = []
    def viewGrades(student):
        pass

    def view_grade(student):
        pass
    def add_to_gradebook(student):
        self.student_grades_arr.append(student)
        # Date or Assignment Name
    def set_assignment(**kwargs):
        pass
    def __iter__(self):
        return self.class_roster


    #def add_assignment(self, created_assignment):
        #Get input for weight of assignment and date

class Classroom(object):
    def __init__(self, subject):
        self.subject = subject
        self.teachers = []

    # __Teacher__
    def assign_teacher(self,teacher):
        try:
            self.teachers.append(teacher)
        except:
            print("Problem with adding the teacher :(...")


class Teacher(object):
    def __init__(self, name):
        self.name = name
        self.class_roster = []
        # __Student Object__

        # Student_Object or Date__of_Grades
    def create_gradebook(self,gradebook_entry):
        self.gradebook = gradebook_entry

    def view_grades(*args, **kwds):
        self.gradebook.view_grades(student)
        # View a single Student_Object)
    # def viewGrade(*args, **kwds):

    def update_student(self, student,edited_student):
        if(self.in_roster(student)):
            self.gradebook.class_roster[student] = edited_student
            print("Sucessfully updated !")

    # __GradeBook__
    def add_to_gradebook(self,student):
        self.gradebook.append(student)
        
    def remove_from_gradebook(self,student):
        if student in self.gradebook:
            gradebook.remove(student)
            print("Sucessfully removed the grade from the gradebook")

    def delete_assignemnt(assignment):
        del self.assignment[assignment]

    def update_gradebook_entry(self,student):
        if(in_gradebook):
            gradebook[student].remove(student)

    def add_assignemnt(assignemnt):
        if not self.in_assignment(assignemnt):
            self.assignments.append(assignemnt)



class Student(object):
    def __init__(self, student_name, enrolled_date):
        self.name = student_name
        self.enrolled_date = enrolled_date
        self.assignments = {}

    def in_assignment(assignment):
        return assignment in self.assignments

    def __str__(self):
        output = "Student Name: {}, Date Enrolled {}".format(self.name, self.enrolled_date)
        return(output)

#    def update_assignment(**kwargs): ## Date

#    def viewGrades(student_name):

#    def viewGrades(*args, **kwargs):

class Assignment(object):
    def __init__(self, assignment_name, grade, assignment_date, description):
        self.assignment_name = assignent_name
        self.date_of_assignment = assignment_date
        self.grade = grade
        self.description = description
        for key, value in kwargs.items():
              setattr(self, key, value)

    def __str__(self):
       return {"Assignment":self.assignment_name,"Grade":grade, "Date":self.assignemnt_date, "Desc":self.drecription}
#    def modify_student_grade(grade):

 #   def modiy_assignment_description(assingment_description):
