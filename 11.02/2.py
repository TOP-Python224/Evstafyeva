from datetime import datetime as dt

class Day_time:
    """Определяет текущий период суток — утро, день, вечер, ночь — для времени в том или ином часовом поясе."""

    def __init__(self, user_time) -> None:
        self.user_time = user_time
        self.start_point = None

    def base_time_zone(self, start_point):
        """Принимает параметр, задающий смещение от текущего часового пояса.
        Текущий часовой пояс — это часовой пояс компьютера, на котором запущен скрипт бота. Определяет период суток
        пользователя. """

        self.start_point = start_point
        start_point = dt.now().hour
        if self.start_point and self.user_time in range(0, 6):
            print('Good night!')
        if self.start_point and self.user_time in range(6, 12):
            print('Good morning!')
        if self.start_point and self.user_time in range(12, 18):
            print('Good day!')
        if self.start_point and self.user_time in range(18, 24):
            print('Good evening!')
        return start_point

    def delta_time(self) -> int:
        return abs(self.user_time - self.start_point)

# тест
user = Day_time(3)
bot = user.base_time_zone(dt.now().hour)
delta_user_bot = user.delta_time()
print(f'Разница во времени человека и бота: {delta_user_bot} ч')

# Извините, случайно обновила старую версию в репозиторие.

# КОММЕНТАРИЙ: ждал-ждал правки, так и не дождался =(
# СДЕЛАТЬ: работу над ошибками в этой задаче, комментарии по ней давал в индивидуальном занятии, пересмотрите запись занятия


# ИТОГ: в ожидании правок — 1/7
