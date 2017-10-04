from teacher import *
from student import *
from assignment import *

def menu():

    clear()
    menu_list = {
        0:add_students,
        1:remove_students,
        2:add_assignment
        }
    
    print("Hello {}. What would you like to do?")
    print("0. Add Student \n 1. Remove Student \n 2. Add Assignments")
    option = int(input(">"))
    menu_list[option]()

def add_students(student_amt):
    student_amt = int(input("How many students would you like to input?: "))
    for _ in range(student_amt):
        student_name = input("What is the name of the student:")
        teach.add_student_to_roster(student_name)
def remove_student():
    teach.get_roster()
    rm_student = input("Which student would you like to remove?")
    teach.
def add_assignment():
    teach.add_assignment(input("What would you like to name the assignment"))



teacher_name = input("What is the teachers name?")
teach = Teacher(teacher_name)
menu()
teach.add_assignment('HW 1')
teach.add_assignment('HW
teach.view_assignment('HW 1')

