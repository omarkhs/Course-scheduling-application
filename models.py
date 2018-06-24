# Course model
import datetime
import calendar

from enum import Enum
from datetime import timedelta


class ActivityType(Enum):
    """ An enum type for different types of sections: lab, lecture, tutorial"""
    LECTURE = "Lecture"
    TUTORIAL = "Tutorial"
    LAB = "Lab"


class Course():
    """ A class for courses """

    # TODO: add rest of attributes and methods
    def __init__(self, department, course_number, title):
        """ Initialize Course and its attributes"""
        self.department = department
        self.course_number = course_number
        self.title = title
        self.activites = []

    def add_activity(self, activity):
        self.activities.append(activity)


class Activity():
    """ A class for activities. An activity can be either a lecture, lab, tutorial"""
    # TODO: add rest of methods
    def __init__(self, section_number, section_type):
        """ Initialize Activity and its attributes.
            section_type refers to whether it is a lab, lecture, or tutorial
        """
        self.section_number = section_number
        self.section_type = section_type

    def is_lab(self):
        """
        Returns true if the activity is a lab
        """
        # TODO:
        return self.section_type == ActivityType.LAB

    # TODO the rest of checks
    #TODO link the associated ActivityTime so the mapping is one to one

class ActivityTime():
    """ a class for time and days of the activity"""

    def __init__(self, activity): # passing the activity that will be associated with the activityTime object
        """ Initialize ActivityTime and its attributes"""
        self.activity = activity
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

    def get_associated_activity(self):
        """
        :return: the associated activity with the ActivityTime
        """
        return self.activity

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
        assert (self.end_time > self.start_time)
        return self.end_time - self.start_time


class TimeTable():
    def __init__(self, days):
        self.days_dict = {'sun': [], 'mon': [], 'tue': [], 'wed': [],'thu': [],'fri': [],'sat': []}

    def add_activity(self, activityTime):
        """
        Adds the activity object associated with the passed activityTime
        to the corresponding day in the TimeTable object
        """
        activity_days = activityTime.get_days()
        for day in activity_days:  # iterate over the list of days of the given activity
            if day in self.days_dict:  # Just in case there is a discrepancy in naming

                # activity object is added to the end of corresponding day list
                self.days_dict[day].append(activityTime.get_associated_activity())

            else:
                break  # maybe print an error ?

    def remove_activity(self, activityTime):
        """
        removes activity from the time table
        """
        activity_days = activityTime.get_days()
        for day in activity_days:
            if day in self.days_dict:  # this check is imp to avoid adding extra k:v to the dict beyond the 7 keys
                day_list = self.days_dict[day]
                day_list.remove(activityTime.get_associated_activity())
                updated_value = {day : day_list}
                self.days_dict.update(updated_value) # updates the value of the key
            else:
                break # maybe print an error ?