from pprint import pprint


class Person:
    def __init__(self,
                 surname: str,
                 name: str,
                 patronymic: str):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

    # @staticmethod
    def is_educating(self):
        # КОММЕНТАРИЙ: ваше условие можно озвучить следующим образом: "является ли объект класса Person объектом класса Student?" — очевидно, что вы всегда будете получать отрицательный ответ
        # ИСПОЛЬЗОВАТЬ: вам же нужно проверить класс у объекта экземпляра — для этого нужен не статический, а обычный метод
        # if Person is Student:
        #     return True
        # else:
        #     return False
        # ИСПОЛЬЗОВАТЬ: однозначную проверку только одного класса
        # return self.__class__ is Student
        # или ИСПОЛЬЗОВАТЬ: проверку на принадлежность к указанному классу или любого его подкласса — предпочтительный вариант
        return isinstance(self, Student)

    # ИСПРАВИТЬ: по аналогии с предыдущим методом
    @staticmethod
    def is_employed():
        if Person is Employee:
            return True
        else:
            return False

    def __str__(self):
        return f'<{self.name} {self.surname} {self.patronymic}>'


class Student(Person):
    def __init__(self,
                 surname: str,
                 name: str,
                 patronymic: str,
                 educational_organization: str,
                 commercial: bool = False):
        super().__init__(surname, name, patronymic)
        self.educational_organization = educational_organization
        self.commercial = commercial

    def __str__(self):
        # ИСПОЛЬЗОВАТЬ: функцию super() можно использовать с любым методом родительского класса, включая и __str__() тоже:
        fullname = super().__str__()[1:-1]
        return f'<{fullname} учится в {self.educational_organization}>'


class Employee(Person):
    def __init__(self,
                 surname: str,
                 name: str,
                 patronymic: str,
                 company: str,
                 salary: int):
        super().__init__(surname, name, patronymic)
        self.company = company
        self.salary = salary

    def __str__(self):
        # ИСПРАВИТЬ: по аналогии с предыдущим классом
        return f'<{self.name} {self.surname} {self.patronymic} работает в {self.company} с окладом в {self.salary} рублей>'


# тест
student1 = Student('Иванов', 'Иван', 'Иванович', 'МГУ', True)
print(student1)
# print(student1.__dict__)

# проверка на принадлежность студента к обучающимся не работает
person1 = student1.is_educating()
print(person1)
print()

employee1 = Employee('Петров', 'Петр', 'Петрович', 'Сбербанк', 100000)
print(employee1)

# проверка на принадлежность сотрудника к работающим не работает
person2 = employee1.is_employed()
print(person2)

# собственное пространство имён объекта класса
# pprint(Student.__dict__)
# область видимости объекта класса
# pprint(dir(Student))


# ИТОГ: конструкторы реализованы верно, остальное не очень, необходимо провести работу над ошибками — 4/7
