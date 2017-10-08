#       Documentation for the Classroom object
#       functions:
#           add_student()
#           remove_assignments()
#           edit_grade()
#           add_grade()
import time
import os
from teacher import *
from student import *

from assignment import *

def clear():
    time.sleep(2)
    os.system("clear")
def menu():
    clear()
    menu_list = {
        0: add_students,
        1: remove_student,
        2: add_assignment,
        3: view_roster,
        4: view_grades,
        5: edit_grade
    }
    
    print("Hello {}. What would you like to do?".format(teacher_name))
    print("0. Add Student \n1. Remove Student \n2. Add Assignments")
    print("3. View Student Roster \n4. View Grades\n5. Edit Grade")
    option = int(input(">"))
    try:
        menu_list[option]()
    except:
        print("Choose a number in the list or add students")

    # Add Students to roster. Ask to update student grade if they are not an assignment
def add_students():
    student_amt = int(input("How many students would you like to input?: "))
    clear()
    to_update = False
    if(teacher.has_assignments()):
        to_update = True if input("Would you like to add students grades also?").lower() == 'y' else False

    for _ in range(student_amt):
        student_name = input("What is the name of the student:")
        teacher.add_student_to_roster(student_name)
        if(to_update):
            teacher.update_missing_assignments(student_name)
    
    # Remove Student from roster
def remove_student():
    if(teacher.get_roster()):
        print(teacher.get_roster());
        rm_student = input("Which student would you like to remove?")
        teacher.remove_student_from_roster(rm_student)
        teacher.remove_student_assingments(rm_student)
    else:
        print("There are no students in the roster")

def add_assignment():
    assignment = teacher.add_assignment(input("What would you like to name the assignment"))
    for student in teacher.get_roster():
        teacher.update_assignment(assignment, student)
        
def view_roster():
    print(teacher.get_roster())

def view_grades():
    print("Which grades would you like to view")
    print(" 0. All\n 1. Specific")
    option = int(input("> "))
    if(option == 0):
        print(teacher.get_assignments())
    elif(option ==1):
        print(teacher.get_roster())
    else:
        print("sorry {} is not an option".format(option))

def edit_grade():
    print(teacher.get_assignments())
    option = input("Which assignment would you like to edit")

teacher_name = input("What is the teachers name?")
teacher = Teacher(teacher_name)

while(True):
    menu()

