from gradedz import *

classrm = Classroom('English')
emily = Teacher('Emily')
classrm.assign_teacher(emily)
gradebook = Gradebook()
emily.add_gradebook(gradebook)
joe = Student("Joe","December 11")
emily.add_assignment(Assignment("Math",97,"October 31","Hello"))
emily.add_student_to_roster(joe)
new_joe = Student("Joe","November")
emily.add_assignment()

Assignment 