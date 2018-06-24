# Course model
import datetime
import calendar

from enum import Enum
from datetime import timedelta


class Course():
    """ A class for courses """

    def __init__(self, department, course_number, title):
        """
        :param department: e.g. CPSC, MATH, ENGL, etc..
        :param course_number: e.g. 110, 121, 210, etc..
        :param title: e.g. Software Construction, Strategies for University Writing, etc..
        """
        self.department = department
        self.course_number = course_number
        self.title = title
        self.activities = []  # List of activities for the course (e.g. different lab/lecture/tutorial sections)

    def add_activity(self, activity):
        """
        Adds an activity associated with the course
        :param activity: lecture or lab or tutorial that is associated with the course
        """
        self.activities.append(activity)

    def remove_activity(self, activity):
        """
        Removes an activity from the list of activities
        """
        self.activities.remove(activity)

    def get_activities(self):
        """
        :returns: list of activities associated with the course
        """
        return self.activities


class ActivityType(Enum):
    """ An enum type for different types of activities: lecture, lab, tutorial"""
    LECTURE = "Lecture"
    LAB = "Lab"
    TUTORIAL = "Tutorial"


class Activity():
    """ A class for activities which can be either a lecture, lab, tutorial"""

    def __init__(self, activity_number, activity_type):
        """
        :param activity_number: this refers to the section number (e.g. L1B, T1A, etc..)
        :param activity_type: Either lecture, lab, or tutorial
        """
        self.activity_number = activity_number
        self.activity_type = activity_type

    def is_lecture(self):
        """ :returns true if the activity is a lecture"""
        return self.activity_type == ActivityType.LECTURE

    def is_tutorial(self):
        """ :returns true if the activity is a tutorial"""
        return self.activity_type == ActivityType.TUTORIAL

    def is_lab(self):
        """ :returns true if the activity is a lab"""
        return self.activity_type == ActivityType.LAB


class ActivityTime():
    """ a class for time and days of the activity"""

    def __init__(self, activity):
        """
        Initialize ActivityTime and its attributes
        :param activity:  The activity that will be associated with the activityTime object
        """
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
        returns the associated activity with the ActivityTime
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
    def __init__(self):
        self.days_dict = {'sun': [], 'mon': [], 'tue': [], 'wed': [], 'thu': [], 'fri': [], 'sat': []}

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
                break  # maybe print an error or throw an exception ?

    def remove_activity(self, activityTime):
        """
        removes activity from the time table
        """
        activity_days = activityTime.get_days()
        for day in activity_days:
            if day in self.days_dict:  # this check is imp to avoid adding extra k:v to the dict beyond the 7 keys
                day_list = self.days_dict[day]
                day_list.remove(activityTime.get_associated_activity())
                updated_value = {day: day_list}
                self.days_dict.update(updated_value)  # updates the value of the key
            else:
                break   # maybe print an error or throw an exception ?
