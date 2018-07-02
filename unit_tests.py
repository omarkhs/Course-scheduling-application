import unittest
from datetime import datetime
from models import Course
from models import Section
from models import SectionType
from models import SectionTime
from models import TimeTable


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def setUp(self):
        self.course = Course("CPSC", "210")
        self.assertEqual(self.course.department, "CPSC")
        self.assertEqual(self.course.course_number, "210")

        self.section = Section("L1A", SectionType.LAB)
        self.assertEqual(self.section.is_lab(), True)

        self.course.add_section(self.section)
        self.assertEquals(len(self.course.get_sections()), 1)

        self.time_table = TimeTable()
        self.mon = self.time_table.days_dict.get(0)
        self.tue = self.time_table.days_dict.get(1)
        self.wed = self.time_table.days_dict.get(2)
        self.thu = self.time_table.days_dict.get(3)
        self.fri = self.time_table.days_dict.get(4)
        self.sat = self.time_table.days_dict.get(5)
        self.sun = self.time_table.days_dict.get(6)

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

        self.set_section_time(self.section, 2, 12, 13)
        self.assertEquals(len(self.section.get_section_times()), 1)

        self.set_section_time(self.section, 2, 13, 14)
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
        self.set_section_time(self.section, 3, 12, 13)
        section_times = self.section.get_section_times()
        self.assertEquals(len(section_times), 1)

        section_time = section_times[0]
        self.assertEquals(section_time.get_duration().total_seconds(), 3600)

    def test_add_course_to_timeTable(self):
        self.set_section_time(self.section, 3, 12, 13)  # occurs on a tue
        self.set_section_time(self.section, 5, 15, 17)  # occurs on a thu
        self.assertEquals(len(self.section.get_section_times()), 2)
        self.time_table.add_course_sections(self.course)

        self.assertEquals(len(self.mon), 0)
        self.assertEquals(len(self.tue), 1)
        self.assertEquals(len(self.wed), 0)
        self.assertEquals(len(self.thu), 1)
        self.assertEquals(len(self.fri), 0)

    def test_add_non_conflicting_courses_to_timeTable(self):
        self.set_section_time(self.section, 3, 12, 13)  # occurs on a tue
        self.set_section_time(self.section, 5, 15, 17)  # occurs on a thu
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
        self.set_section_time(self.section, 3, 12, 13)  # occurs on a tue
        self.set_section_time(self.section, 5, 15, 17)  # occurs on a thu
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

        # year, month, day, hour(24hr time)
        start_time = datetime(2018, 7, day, start_hour)
        end_time = datetime(2018, 7, day, end_hour)

        # note: a section time is added to the associated section when section time object is constructed
        section_time = SectionTime(section, start_time, end_time)
        section_time.add_day(start_time.weekday())

    def populate_each_day_in_time_table(self):
        comm_course = Course("COMM", "458")
        comm_section = Section("T2C", SectionType.TUTORIAL)
        comm_course.add_section(comm_section)
        self.set_section_time(comm_section, 2, 13, 14)  # occurs on a mon
        self.set_section_time(comm_section, 4, 13, 14)  # occurs on a wed
        self.set_section_time(comm_section, 6, 13, 14)  # occurs on a fri
        self.time_table.add_course_sections(comm_course)

        cpsc_course = Course("CPSC", "310")
        cpsc_section = Section("101", SectionType.LECTURE)
        cpsc_course.add_section(cpsc_section)
        self.set_section_time(cpsc_section, 3, 13, 14)  # occurs on a tue
        self.set_section_time(cpsc_section, 5, 13, 14)  # occurs on a thu
        self.time_table.add_course_sections(cpsc_course)


if __name__ == '__main__':
    unittest.main()
