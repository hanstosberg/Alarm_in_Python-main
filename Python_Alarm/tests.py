from Alarm_Clock import AlarmClock
import unittest

class AlarmClockTest(unittest.TestCase):
    def test_alarm_clock(self):
        self.alarm_clock = AlarmClock()
        result = self.alarm_clock.minutesLeft('10:00:00',"12", "00")
        self.assertEqual(result, 120)
        result = self.alarm_clock.minutesLeft('10:00:00',"13", "30")
        self.assertEqual(result, 210)
        result = self.alarm_clock.minutesLeft('10:00:00',"10", "37")
        self.assertEqual(result, 37)


if __name__ == "__main__":
  unittest.main()