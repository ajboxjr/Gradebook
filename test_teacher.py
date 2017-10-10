import unittest
from student import *
from teacher import *

class TestTeacher(unittest.TestCase):
    def setUp(self):
        self.teacher = Teacher('Janny')

    def test_add_student(self):
        result = self.teacher.add_student_to_roster(Student('Bob'))
        self.assertEqual(len(teacher.class_roster),2)
    def test_remove_student(self):
        self.teacher.remove_student_from_roster(Student('Joe'))
        self.assertEqual('joe' in self.teacher.class_roster, True)

if __name__ == '__main__':
    unittest.main()
