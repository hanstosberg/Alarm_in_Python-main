from Alarm_Clock import AlarmClock
import unittest
import sys


class AlarmClockTest(unittest.TestCase):
    def test_alarm_clock(self):
        self.alarm_clock = AlarmClock()
        result = self.alarm_clock.minutesLeft('10:00:00',"12", "00")
        self.assertEqual(result, 120)
        result = self.alarm_clock.minutesLeft('10:00:00',"13", "30")
        self.assertEqual(result, 210)
        result = self.alarm_clock.minutesLeft('10:00:00',"10", "37")
        self.assertEqual(result, 37)

    def test_time_checker(self):
        result = self.alarm_clock.time_checker('10:00:00','10', "13", True)
        self.assertEqual(result, False)
        result = self.alarm_clock.time_checker('10:00:00','10', "10", True)
        self.assertEqual(result, False)
        result = self.alarm_clock.time_checker('10:00:00','10', "00", True)
        self.assertEqual(result, True)

if __name__ == "__main__":
  unittest.main()