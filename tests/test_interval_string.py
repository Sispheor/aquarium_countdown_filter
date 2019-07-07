import unittest

from utils.interval_string import IntervalString


class TestIntervalString(unittest.TestCase):

    def test_get_second_from_sting(self):

        self.assertEqual(10, IntervalString.get_second_from_sting("10s"))
        self.assertEqual(172800, IntervalString.get_second_from_sting("2d"))
        self.assertIsNone(IntervalString.get_second_from_sting("10"))
        self.assertIsNone(IntervalString.get_second_from_sting("s"))
        self.assertIsNone(IntervalString.get_second_from_sting("23j"))
        self.assertIsNone(IntervalString.get_second_from_sting("24gg"))
        self.assertIsNone(IntervalString.get_second_from_sting("24gg23"))
