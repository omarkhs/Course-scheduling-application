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
        self.course = models.Course("CPSC","210")
        self.assertEqual(self.course.department, "CPSC")
        self.assertEqual(self.course.course_number, "210")

        self.activity = models.Activity("L1A", models.ActivityType.LAB)
        self.assertEqual(self.activity.is_lab(), True)

        self.course.add_activity(self.activity)
        self.assertEquals(len(self.course.get_activities()), 1)

    def test_adding_activities(self):
        tutorial = models.Activity("T1B", models.ActivityType.TUTORIAL)
        self.assertEqual(tutorial.is_tutorial(), True)
        self.course.add_activity(tutorial)
        self.assertEquals(len(self.course.get_activities()), 2)

    def test_removing_activities(self):
        self.course.remove_activity(self.activity)
        self.assertEquals(len(self.course.get_activities()), 0)

if __name__ == '__main__':
    unittest.main()
