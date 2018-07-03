import unittest
import calendar
from datetime import datetime
from models import Course
from models import Section
from models import SectionType
from models import SectionTime
from models import TimeTable


class TestModels(unittest.TestCase):

    def setUp(self):
        self.course = Course("CPSC", "210")
        self.assertEqual(self.course.department, "CPSC")
        self.assertEqual(self.course.course_number, "210")

        self.section = Section("L1A", SectionType.LAB)
        self.assertEqual(self.section.is_lab(), True)

        self.course.add_section(self.section)
        self.assertEquals(len(self.course.get_sections()), 1)

        self.time_table = TimeTable()
        self.mon = self.time_table.days_dict.get(calendar.MONDAY)
        self.tue = self.time_table.days_dict.get(calendar.TUESDAY)
        self.wed = self.time_table.days_dict.get(calendar.WEDNESDAY)
        self.thu = self.time_table.days_dict.get(calendar.THURSDAY)
        self.fri = self.time_table.days_dict.get(calendar.FRIDAY)
        self.sat = self.time_table.days_dict.get(calendar.SATURDAY)
        self.sun = self.time_table.days_dict.get(calendar.SUNDAY)

    def test_adding_sections_to_course(self):
        self.assertEquals(len(self.course.get_sections()), 1)

        tutorial = Section("T1B", SectionType.TUTORIAL)
        self.assertEqual(tutorial.is_tutorial(), True)
        self.course.add_section(tutorial)

        self.assertEquals(len(self.course.get_sections()), 2)

    def test_removing_sections_from_course(self):
        self.assertEquals(len(self.course.get_sections()), 1)
        self.course.remove_section(self.section)
        self.assertEquals(len(self.course.get_sections()), 0)

    def test_add_section_time(self):
        self.assertEquals(len(self.section.get_section_times()), 0)

        self.set_section_time(self.section, calendar.MONDAY, 12, 13)
        self.assertEquals(len(self.section.get_section_times()), 1)

        self.set_section_time(self.section, calendar.MONDAY, 13, 14)
        self.assertEquals(len(self.section.get_section_times()), 2)

    def test_remove_section_time(self):
        start_time = datetime(2018, 7, 2, 12)
        end_time = datetime(2018, 7, 2, 13)

        # note: a section time is added to the associated section when section time object is constructed
        section_time = SectionTime(self.section, start_time, end_time)
        self.assertEquals(len(self.section.get_section_times()), 1)

        self.section.remove_section_time(section_time)
        self.assertEquals(len(self.section.get_section_times()), 0)

    def test_get_duration_of_section(self):
        self.set_section_time(self.section, calendar.TUESDAY, 12, 13)
        section_times = self.section.get_section_times()
        self.assertEquals(len(section_times), 1)

        section_time = section_times[0]
        self.assertEquals(section_time.get_duration().total_seconds(), 3600)

    def test_add_course_to_timeTable(self):
        self.set_section_time(self.section, calendar.TUESDAY, 12, 13)
        self.set_section_time(self.section, calendar.THURSDAY, 15, 17)
        self.assertEquals(len(self.section.get_section_times()), 2)
        self.time_table.add_course_sections(self.course)

        self.assertEquals(len(self.mon), 0)
        self.assertEquals(len(self.tue), 1)
        self.assertEquals(len(self.wed), 0)
        self.assertEquals(len(self.thu), 1)
        self.assertEquals(len(self.fri), 0)

    def test_add_non_conflicting_courses_to_timeTable(self):
        self.set_section_time(self.section, calendar.TUESDAY, 12, 13)
        self.set_section_time(self.section, calendar.THURSDAY, 15, 17)
        self.time_table.add_course_sections(self.course)

        self.populate_each_day_in_time_table()

        self.assertEquals(len(self.mon), 1)
        self.assertEquals(len(self.tue), 2)
        self.assertEquals(len(self.wed), 1)
        self.assertEquals(len(self.thu), 2)
        self.assertEquals(len(self.fri), 1)
        self.assertEquals(len(self.sat), 0)
        self.assertEquals(len(self.sun), 0)

    def test_remove_course_from_timeTable(self):
        self.set_section_time(self.section, calendar.TUESDAY, 12, 13)
        self.set_section_time(self.section, calendar.THURSDAY, 15, 17)
        self.time_table.add_course_sections(self.course)

        self.populate_each_day_in_time_table()

        self.assertEquals(len(self.mon), 1)
        self.assertEquals(len(self.tue), 2)
        self.assertEquals(len(self.wed), 1)
        self.assertEquals(len(self.thu), 2)
        self.assertEquals(len(self.fri), 1)
        self.assertEquals(len(self.sat), 0)
        self.assertEquals(len(self.sun), 0)

        self.time_table.remove_course_sections(self.course)

        self.assertEquals(len(self.mon), 1)
        self.assertEquals(len(self.tue), 1)
        self.assertEquals(len(self.wed), 1)
        self.assertEquals(len(self.thu), 1)
        self.assertEquals(len(self.fri), 1)
        self.assertEquals(len(self.sat), 0)
        self.assertEquals(len(self.sun), 0)

    # a method that creates section time and adds it to self.section
    # later I will create a method that randomly generates data
    def set_section_time(self, section, day, start_hour, end_hour):
        year = 2018
        month = 7
        # this is to convert calendar.WEEKDAY to the corresponding day in first week of July 2018
        # e.g. calendar.MONDAY = 0 but Monday in first week of july is the 2nd of July
        day = day + 2
        start_time = datetime(year, month, day, start_hour)
        end_time = datetime(year, month, day, end_hour)

        # note: a section time is added to the associated section
        # when section time object is constructed
        section_time = SectionTime(section, start_time, end_time)
        section_time.add_day(start_time.weekday())

    def populate_each_day_in_time_table(self):
        comm_course = Course("COMM", "458")
        comm_section = Section("T2C", SectionType.TUTORIAL)
        comm_course.add_section(comm_section)
        self.set_section_time(comm_section, calendar.MONDAY, 13, 14)  # occurs on a mon
        self.set_section_time(comm_section, calendar.WEDNESDAY, 13, 14)  # occurs on a wed
        self.set_section_time(comm_section, calendar.FRIDAY, 13, 14)  # occurs on a fri
        self.time_table.add_course_sections(comm_course)

        cpsc_course = Course("CPSC", "310")
        cpsc_section = Section("101", SectionType.LECTURE)
        cpsc_course.add_section(cpsc_section)
        self.set_section_time(cpsc_section, calendar.TUESDAY, 13, 14)  # occurs on a tue
        self.set_section_time(cpsc_section, calendar.THURSDAY, 13, 14)  # occurs on a thu
        self.time_table.add_course_sections(cpsc_course)


if __name__ == '__main__':
    unittest.main()
