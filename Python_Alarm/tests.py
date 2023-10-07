from Alarm_Clock import AlarmClock
import unittest
import sys
import datetime
import datetime
import subprocess

time_tuple = ( 2023, # Year
                  10, # Month
                  7, # Day
                  10, # Hour
                 00, # Minute
                  0, # Second
                  0, # Millisecond
               )

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
        self.alarm_clock = AlarmClock()
        result = self.alarm_clock.time_checker('10:00:00','10', "13", True)
        self.assertEqual(result, True)
        result = self.alarm_clock.time_checker('10:00:00','10', "10", True)
        self.assertEqual(result, True)
        result = self.alarm_clock.time_checker('10:00:00','10', "00", True)
        self.assertEqual(result, False)



if __name__ == "__main__":
    # Получаем текущую дату и время
    now = datetime.datetime.now()

    # Создаем новую дату и время
    new_date = now.replace(year=2023, month=9, day=7)
    new_time = now.replace(hour=10, minute=0, second=0)

    # Форматируем новую дату и время в нужный формат
    date_str = new_date.strftime("%m%d%Y")
    time_str = new_time.strftime("%H%M%S")

    # Используем команды операционной системы для изменения системной даты и времени
    subprocess.call(["date", date_str])
    subprocess.call(["time", time_str])
    unittest.main()