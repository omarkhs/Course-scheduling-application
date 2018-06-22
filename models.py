# Course model
import datetime
import calendar

from enum import Enum
from datetime import timedelta

class SectionType(Enum):
    """ An enum type for different types of sections: lab, lecture, tutorial"""
    LECTURE = "Lecture"
    TUTORIAL = "Tutorial"
    LAB = "Lab"

class ActivityTime():
   """ a class for time and days of the activity"""

    def __init__(self):
      """ Initialize ActivityTime and its attributes"""
      self.days = []
      self.start_time = None
      self.end_time = None

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

    def get_duration(self):
        """
        returns the duration of the activity
        which is the difference between the start and end time
        """
        assert(end_time > start_time)
        return end_time - start_time

class Activity():
    """ A class for activities. An activity can be either a lecture, lab, tutorial"""
    # TODO: add rest of methods
    def __init__(self, section_number, section_type)
        """ Initialize Activity and its attributes.
            section_type refers to whether it is a lab, lecture, or tutorial
        """
        self.section_number = section_number
        self.section_type = section_type

    def is_lab( self ):
        """
        Returns true if the activity is a lab
        """
        #TODO:
        return self.section_type == SectionType.LAB

    #TODO the rest of checks

class Course():
    """ A class for courses """
    # TODO: add rest of attributes and methods
    def __init__(self, department, course_number, title):
        """ Initialize Course and its attributes"""
        self.department = department
        self.course_number = course_number
        self.title = title
        self.activites = []

    def add_activity( self, activity ):
        self.activities.append( activity )