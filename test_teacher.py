import unittest
import teacher
import student
class TestTeacher(unittest.TestCase):
    def setUp(self):
        self.teacher = teacher.Teacher('Janny')


    def test_add_student_to_roster(self):
        result = self.teacher.add_student_to_roster(Student('Bob'))
        self.assertEqual(len(teacher.class_roster),1)

if __name__ == '__main__':
    unittest.main()
