# Course model
from enum import Enum

class Course():
    """ A class for courses """
# TODO: add rest of attributes and methods
    def __init__(self, name, title, course_number):
        """ Initialize Course and its attributes"""
        self.name = name
        self.title = title
        self.course_number = course_number


class SectionType(Enum):
    """ An enum type for different types of sections: lab, lecture, tutorial"""
    LECTURE = "Lecture"
    TUTORIAL = "Tutorial"
    LAB = "Lab"

# TODO: add rest of methods
class Activity():
    """ A class for activities. An activity can be either a lecture, lab, tutorial"""

    def __init__(self, department, section_number, section_type):
        """ Initialize Activity and its attributes.
            section_type refers to whether it is a lab, lecture, or tutorial
        """
        # should I create a setter/getters for department and section_number ?
        # in 210 we would always use setters and getters. what do you think ?
        self.department = department
        self.section_number = section_number

        # TODO: check how to initialize
        self.section_type = SectionType

    def set_type(self, section_type):
        self.section_type = section_type

    class ActivityTime():
        """ a class for time and days of the activity"""

        def __init__(self):
            """ Initialize ActivityTime and its attributes"""
            self.days = []
            self.start_time = 0  # left it as an int for now but I am thinking of using datetime module of python
            self.end_time = 0  # see comment above

        def set_days(self, list_of_days):
            """ set the days of the activity """
            self.days = list_of_days

        def set_start_time(self, start_time):
            """ set start time of activity """
            self.start_time = start_time

        def set_end_time(self, end_time):
            """ set end time of activity """
            self.end_time = end_time

        def get_days(self):
            """ returns the list of days of the activity"""
            return self.days

        def get_start_time(self):
            """ returns the start time of activity """
            return self.start_time

        def get_end_time(self):
            """ returns end time of activity """
            return self.end_time
