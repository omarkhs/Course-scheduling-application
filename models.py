# Course model
from enum import Enum


class Course:
    """ A class for courses """

    def __init__(self, department, course_number, title=""):
        """
        :param department: e.g. CPSC, MATH, ENGL, etc..
        :param course_number: e.g. 110, 121, 210, etc..
        :param title: e.g. Software Construction, Strategies for University Writing, etc..
        """
        self.department = department
        self.course_number = course_number
        self.title = title
        # List of sections for the course (e.g. different lab/lecture/tutorial sections)
        self.sections = []

    def add_section(self, section):
        """
        Adds a section associated with the course
        :param section: lecture or lab or tutorial that is associated with the course
        """
        self.sections.append(section)

    def remove_section(self, section):
        """
        Removes a section from the list of sections
        """
        self.sections.remove(section)

    def get_sections(self):
        """
        :returns: list of sections associated with the course
        """
        return self.sections

    def get_department(self):
        """
        :returns: department in which this course is under
        """
        return self.department

    def get_course_number(self):
        """
        :returns: course number
        """
        return self.course_number


class SectionType(Enum):
    """ An enum type for different types of sections: lecture, lab, tutorial"""
    LECTURE = "Lecture"
    LAB = "Lab"
    TUTORIAL = "Tutorial"


class Section:
    """ A class for sections which can be either a lecture, lab, tutorial"""

    def __init__(self, section_number, section_type):
        """
        :param section_number: this refers to the section number (e.g. L1B, T1A, etc..)
        :param section_type: Either lecture, lab, or tutorial
        """
        self.section_number = section_number
        self.section_type = section_type

    def is_lecture(self):
        """ :returns true if the section is a lecture"""
        return self.section_type == SectionType.LECTURE

    def is_tutorial(self):
        """ :returns true if the section is a tutorial"""
        return self.section_type == SectionType.TUTORIAL

    def is_lab(self):
        """ :returns true if the section is a lab"""
        return self.section_type == SectionType.LAB


class SectionTime:
    """ a class for time and days of the section"""

    def __init__(self, section):
        """
        Initialize SectionTime and its attributes
        :param section:  The section that will be associated with the sectionTime object
        """
        self.section = section
        self.days = []
        self.start_time = None
        self.end_time = None

    def set_days(self, list_of_days):
        """ set the days of the section """
        self.days = list_of_days

    def set_start_time(self, start_time):
        """ set start time of section """
        self.start_time = start_time

    def set_end_time(self, end_time):
        """ set end time of section """
        self.end_time = end_time

    def get_associated_section(self):
        """
        returns the associated section with the SectionTime
        """
        return self.section

    def get_days(self):
        """ returns the list of days of the section"""
        return self.days

    def get_start_time(self):
        """ returns the start time of section """
        return self.start_time

    def get_end_time(self):
        """ returns end time of section """
        return self.end_time

    def get_duration(self):
        """
        returns the duration of the section
        which is the difference between the start and end time
        """
        assert (self.end_time > self.start_time)
        return self.end_time - self.start_time


class TimeTable:
    def __init__(self):
        #  TODO use the calendar module
        self.days_dict = {'sun': [], 'mon': [], 'tue': [], 'wed': [], 'thu': [], 'fri': [], 'sat': []}

    def add_section(self, section_time):
        """
        Adds the section object associated with the passed section_time
        to the corresponding day in the TimeTable object
        """
        section_days = section_time.get_days()
        # iterate over the list of days of the given section
        for day in section_days:
            # Just in case there is a discrepancy in naming
            if day in self.days_dict:

                # section object is added to the end of corresponding day list
                self.days_dict[day].append(section_time.get_associated_section())

            else:
                # maybe print an error or throw an exception ?
                break

    def remove_section(self, section_time):
        """
        removes section from the time table
        """
        section_days = section_time.get_days()
        for day in section_days:
            # this check is imp to avoid adding extra key:value to the dict beyond the 7 keys
            if day in self.days_dict:
                day_list = self.days_dict[day]
                day_list.remove(section_time.get_associated_section())
                updated_value = {day: day_list}
                # updates the value of the key
                self.days_dict.update(updated_value)

            else:
                # maybe print an error or throw an exception ?
                break
