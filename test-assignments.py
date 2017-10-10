import pytest
from teacher import *

def create_teacher():
	teacher = teacher("Joe")
	return teacher

assert(create_teacher(),teacher('Joe'))

# def test_add_student():
# 	teacher = create_teacher()
# 	student = create_student()
# 	teacher.add_student_to_roster()

# def test_remove_student():
# 	teacher = create_teacher()
# 	assertEqual('Joe', student)
# 	student = create_student('Joe')
# 	teacher.remove_student_from_roster()


