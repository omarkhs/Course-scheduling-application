import unittest
import models

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
        self.course = models.Course("CPSC", "210")
        self.assertEqual(self.course.department, "CPSC")
        self.assertEqual(self.course.course_number, "210")

        self.activity = models.Section("L1A", models.SectionType.LAB)
        self.assertEqual(self.activity.is_lab(), True)

        self.course.add_section(self.activity)
        self.assertEquals(len(self.course.get_sections()), 1)

    def test_adding_activities(self):
        tutorial = models.Section("T1B", models.SectionType.TUTORIAL)
        self.assertEqual(tutorial.is_tutorial(), True)
        self.course.add_section(tutorial)
        self.assertEquals(len(self.course.get_sections()), 2)

    def test_removing_activities(self):
        self.course.remove_section(self.activity)
        self.assertEquals(len(self.course.get_sections()), 0)


if __name__ == '__main__':
    unittest.main()
