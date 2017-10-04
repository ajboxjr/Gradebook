class Assignment(object):
    def __init__(self, name):
        self.__name = name
        self.__assignment_grades = dict()
        self.due_date = 0

    def get_assignments(self):
        return self.__assignment_grades 

    def add_grades_to_student(self, roster_student, grade):
        if roster_student not in self.get_assignments():
            self.set_grade(roster_student, grade)
                    
    def set_grade(self, roster_student,grade):
            self.__assignment_grades[roster_student] = grade
            print("{} :".format(self))
            print("Set {} grade to {}".format(roster_student,grade))
    

    def get_name(self):
        return self.__name
    def __str__(self):
        return self.get_name()
