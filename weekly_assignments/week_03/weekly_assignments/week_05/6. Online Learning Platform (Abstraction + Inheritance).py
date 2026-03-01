from abc import ABC, abstractmethod

# Abstract class
class Course(ABC):
    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

    @abstractmethod
    def course_details(self):
        pass


# Programming Course
class ProgrammingCourse(Course):
    def course_details(self):
        print("Course:", self.course_name)
        print("Duration:", self.duration)
        print("Includes coding practice and projects")


# Design Course
class DesignCourse(Course):
    def course_details(self):
        print("Course:", self.course_name)
        print("Duration:", self.duration)
        print("Includes UI/UX and graphic design concepts")


# Marketing Course
class MarketingCourse(Course):
    def course_details(self):
        print("Course:", self.course_name)
        print("Duration:", self.duration)
        print("Includes digital marketing strategies")


# Creating objects
c1 = ProgrammingCourse("Python Programming", "3 Months")
c2 = DesignCourse("Graphic Design", "2 Months")
c3 = MarketingCourse("Digital Marketing", "1 Month")

courses = [c1, c2, c3]

for c in courses:
    c.course_details()
    print()