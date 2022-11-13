from datetime import datetime as dt


class Day_time:
    """Определяет текущий период суток — утро, день, вечер, ночь — для времени в том или ином часовом поясе."""
    def __init__(self, time_period: tuple) -> None:
        """
        :param night: период с 0:00 до 5:59
        :param morning: период с 6:00 до 11:59
        :param day: период с 12:00 до 17:59
        :param evening: период с 18:00 до 23:59
        """

        self.time_period = time_period
        for time_period in range(0, dt.time[0:3](5, 59, 59)):
            self.time_period = night

        for time_period in range(dt.time[0:3](6, 00, 00), dt.time[0:3](11, 59, 59)):
            self.time_period = morning

        for time_period in range(dt.time[0:3](12, 00, 00), dt.time[0:3](17, 59, 59)):
            self.time_period = day

        for time_period in range(dt.time[0:3](18, 00, 00), dt.time[0:3](23, 59, 59)):
            self.time_period = evening



    def current_period(self, current_time) -> str:
        """Определяет период суток. Принимает параметр, задающий смещение от текущего часового пояса.
        Текущий часовой пояс — это часовой пояс компьютера, на котором запущен скрипт бота."""
        current_time = dt.now[3:6]
        if current_time == night:
            print('Good night!')
        if current_time == morning:
            print('Good morning!')
        if current_time == day:
            print('Good day!')
        if current_time == evening:
            print('Good evening!')

    def __str__(self):
        return f'{current_time}'

# time_now =
# my_time_period = Day_time(time_now)
# print(my_time_period)



