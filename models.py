# Course model

import calendar
from enum import Enum


class Course:
    """ A class for courses """

    def __init__(self, department, course_number, title=""):
        """
        :param department: e.g. CPSC, MATH, ENGL, etc..
        :param course_number: e.g. 110, 121, 210, etc..
        :param title: e.g. Software Construction, Strategies for University Writing, etc..
        note: title is optional
        """
        self.department = department
        self.course_number = course_number
        self.title = title
        # List of sections for the course (e.g. different lab/lecture/tutorial sections)
        self.sections = []

    def add_section(self, section):
        """
        Adds a section associated with the course to the end of the list of sections
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
        :return: list of sections associated with the course
        """
        return self.sections

    def get_department(self):
        """
        :return: department in which this course is under
        """
        return self.department

    def get_course_number(self):
        """
        :return: course number
        """
        return self.course_number
    
    def get_title(self):
        """
        :return: title of the course
        """
        return self.title


class SectionType(Enum):
    """ An enum type for different types of sections: lecture, lab, tutorial"""
    LECTURE = "Lecture"
    LAB = "Lab"
    TUTORIAL = "Tutorial"


class Section:
    """
    A class for sections which can be either a lecture, lab, tutorial
    A section can have multiple section times (e.g. CPSC 213 labs they run twice a week with different end times)
    """

    def __init__(self, section_number, section_type):
        """
        :param section_number: this refers to the section number (e.g. L1B, T1A, etc..)
        :param section_type: Either lecture, lab, or tutorial
        """
        self.section_number = section_number
        self.section_type = section_type
        self.section_times = []

    def add_section_time(self, section_time):
        """
        adds section time object to the end list of sections
        :param section_time: section time object associated with this section
        """
        self.section_times.append(section_time)

    def remove_section_time(self, section_time):
        """ removes section time object from the list of sections """
        self.section_times.remove(section_time)

    def get_section_times(self):
        """ :return: list of sections times associated with this section """
        return self.section_times

    def is_lecture(self):
        """ :return true if the section is a lecture"""
        return self.section_type == SectionType.LECTURE

    def is_tutorial(self):
        """ :return true if the section is a tutorial"""
        return self.section_type == SectionType.TUTORIAL

    def is_lab(self):
        """ :return true if the section is a lab"""
        return self.section_type == SectionType.LAB


class SectionTime:
    # TODO in order for the timetable to work we need to be able to compare section time objects
    """ a class for time and days of the section"""

    def __init__(self, section, start_time, end_time):
        """
        Initialize SectionTime and its attributes
        :param section:  The section that will be associated with the sectionTime object
        note: a section time object can only be associated with only one section
        """
        self.days = []
        self.start_time = start_time
        self.end_time = end_time
        self.section = section
        # a section time object is added to the associated section when created
        section.add_section_time(self)

    def set_days(self, list_of_days):
        """ set the days of the section """
        self.days = list_of_days

    def add_day(self, day):
        """ adds a day to the end list of days"""
        self.days.append(day)

    def remove_day(self, day):
        """ removes a day from the list of days """
        self.days.remove(day)

    def set_start_time(self, start_time):
        """ set start time of section """
        self.start_time = start_time

    def set_end_time(self, end_time):
        """ set end time of section """
        self.end_time = end_time

    def get_associated_section(self):
        """
        return the associated section with the SectionTime
        """
        return self.section

    def get_days(self):
        """ return the list of days of the section"""
        return self.days

    def get_start_time(self):
        """ return the start time of section """
        return self.start_time

    def get_end_time(self):
        """ return end time of section """
        return self.end_time

    def get_duration(self):
        """
        return the duration of the section
        which is the difference between the start and end time
        """
        assert (self.end_time > self.start_time)
        return self.end_time - self.start_time


class TimeTable:
    def __init__(self):
        """ Creates a dictionary with the seven days as keys and empty lists as values"""
        self.days_dict = {calendar.MONDAY: [], calendar.TUESDAY: [], calendar.WEDNESDAY: [],
                          calendar.THURSDAY: [], calendar.FRIDAY: [], calendar.SATURDAY: [],
                          calendar.SUNDAY: []}

    def add_course_sections(self, course):
        """
        Adds all sections of the given course to the corresponding day in the TimeTable object
        :param course: given course (e.g. CPSC 210)
        """
        list_of_sections = course.get_sections()
        # iterates over the list of sections in the given course
        for section in list_of_sections:
            list_of_section_times = section.get_section_times()

            # iterates over the list of section times of the section
            for section_time in list_of_section_times:
                list_of_section_days = section_time.get_days

                # iterates over the list of days during which one of the course sections runs
                for day in list_of_section_days:
                    # section time object is added to the list of the corresponding day in the dictionary
                    self.days_dict[day].append(section_time)

    def remove_course_sections(self, course):
        """
        Removes all sections of the given course from the TimeTable object
        :param course: given course (e.g. CPSC 210)
        """
        list_of_sections = course.get_sections()
        for section in list_of_sections:
            list_of_section_times = section.get_section_times()

            for section_time in list_of_section_times:
                list_of_section_days = section_time.get_days

                for day in list_of_section_days:
                    # the check below is important to avoid adding extra key;value pair to the dictionary
                    if day in self.days_dict:
                        # the_list_of_values_of_day == list of section time objects associated with the day (ie key)
                        list_of_values_of_day = self.days_dict[day]

                        # TODO for correct impl need to override comparison method to compare section time objects
                        list_of_values_of_day.remove(section_time)
                        updated_values = {day: list_of_values_of_day}
                        # updates the list of values of the key
                        self.days_dict.update(updated_values)

                    else:
                        # TODO: print an error or throw an exception
                        break
