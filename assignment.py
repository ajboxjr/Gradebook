class Assignment(object):
    def __init__(self, name):
        self.__name = name
        self.__assignment_grades = dict()
        self.due_date = 0

    def get_assignments(self):
        return self.__assignment_grades 

    def set_grade(self, roster_student,grade):
        self.__assignment_grades[roster_student] = grade
        print("{} :".format(self))
        print("Set {} grade to {}".format(roster_student,grade))

    def remove_student(self,student):
        self.__assignment_grades.pop(student,None)
        print("Removed {} from {}".format(student, self.get_name()))
    
    # Get A specific student grade for assignment
    def get_grade(self,student_name):
        return self.__assignment_grades[student_name]

    def get_grades(self):
        return self.__assignment_grades

    def get_name(self):
        return self.__name

    def __str__(self):
        return self.get_name()
