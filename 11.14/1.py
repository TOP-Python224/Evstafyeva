from pprint import pprint


class Person:
    def __init__(self,
                 surname: str,
                 name: str,
                 patronymic: str):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

    @staticmethod
    def is_educating():
        if Person is Student:
            return True
        else:
            return False

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
        return f'<{self.name} {self.surname} {self.patronymic} учится в {self.educational_organization}>'


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
