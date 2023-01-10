from abc import ABC
from datetime import date
from decimal import Decimal
from enum import Enum


class Contact:
    """Содержит контактную информацию о головной и дочерних организациях, их сотрудниках и студентах"""

    def __init__(self,
                 mobile: str = None,
                 email: str = None,
                 office: str = None,
                 home: str = None,
                 telegram: str = None,
                 icq: str = None):
        self.mobile = mobile
        self.email = email
        self.office = office
        self.home = home
        self.telegram = telegram
        self.icq = icq

    # ДОБАВИТЬ: реализации для методов ниже

    def validate_mobile(self) -> bool:
        pass

    def validate_email(self) -> bool:
        pass

    def validate_office(self) -> bool:
        pass

    def validate_home(self) -> bool:
        pass

    def validate_validate_telegram(self) -> bool:
        pass

    def validate_icq(self) -> bool:
        pass


class Person(ABC):
    """Содержит информацию о персональных данных работников и студентов"""

    class Gender(Enum):
        MALE = 'male'
        FEMALE = 'female'

    def __init__(self,
                 surname: str,
                 name: str,
                 patronymic: str,
                 birthdate: date,
                 gender: Gender,
                 contact: Contact):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.birthdate = birthdate
        self.gender = gender
        self.contact = contact


class Employee(ABC, Person):
    """Определяет штатное расписание головной и дочерних организаций"""

    def __init__(self,
                 hire_date: date,
                 # ИСПРАВИТЬ здесь и далее: префиксы _ и __ не имеют смысла для локальных переменных, каковыми являются параметры функций
                 _prev_experience: int,
                 salary: Decimal,
                 position: str,
                 # ИСПРАВИТЬ здесь и далее: аннотация класса, который объявляется позже, осуществляется с помощью строкового литерала с именем класса
                 head: Administrator,
                 # ИСПРАВИТЬ: в конструкторе дочернего класса первым делом перечисляют параметры для конструктора родительского класса, а потом собственные параметры — это даёт сходство сигнатур конструкторов родственных классов
                 surname: str,
                 name: str,
                 patronymic: str,
                 birthdate: date,
                 # ИСПРАВИТЬ: класс Gender объявляется в пространстве имён класса Person, то есть он является атрибутом класса Person — именно как к атрибуту к нему и следует обращаться (или использовать агрегацию или слабую композицию, объявляя класс Gender в пространстве имён модуля, а не другого класса)
                 gender: Gender,
                 contact: Contact):
        self.hire_date = hire_date
        # ИСПРАВИТЬ: а вот для имён атрибутов префиксы _ и __ определяют тип атрибута как "частный" и "защищённый" соответственно
        self.prev_experience = prev_experience
        self.salary = salary
        self.position = position
        self.head = head
        # ИСПРАВИТЬ: заметно более удобной практикой расширения поведения метода-конструктора в дочернем классе является первоочередное использование вызова конструктора родительского класса — вызов super().__init__() следует перенести в начало метода
        super().__init__(surname, name, patronymic, birthdate, gender, contact)

    @property
    def experience(self):
        return None


class GeneralPersonnel(Employee):
    pass


class Administrator(Employee):

    def __init__(self,
                 # ДОБАВИТЬ: все параметры из каждого конструктора каждого родительского класса
                 division: str,
                 subordinates: list[Employee]):
        self.subordinates = subordinates
        self.division = division
        # ИСПРАВИТЬ: перенести вызов super().__init__() в начало конструктора
        super().__init__(
            # КОММЕНТАРИЙ: иначе, откуда интерпретатору взять все эти переменные в локальном пространстве имён функции?
            hire_date,
            _prev_experience,
            salary,
            position,
            head,
            surname,
            name,
            patronymic,
            birthdate,
            gender,
            contact
        )


class ProfessionalEmployee(Employee):
    """Содержит информацию об ученой степени и званиях профессорско-преподавательского состава"""

    # ДОБАВИТЬ: все параметры из каждого конструктора каждого родительского класса
    def __init__(self, degree: Degree):
        self.degree = degree
        # ИСПРАВИТЬ: перенести вызов super().__init__() в начало конструктора
        super().__init__(
            hire_date,
            _prev_experience,
            salary,
            position,
            head,
            surname,
            name,
            patronymic,
            birthdate,
            gender,
            contact
        )


class Researcher(ProfessionalEmployee):
    pass


class Teacher(ProfessionalEmployee):
    """Содержит информацию о преподавателях и курсах, которые они ведут"""

    # ИСПРАВИТЬ: на диаграмме класс Degree включается в класс ProfessionalEmployee с помощью агрегации, а не композиции — это значит, что он должен быть объявлен независимо от классов ProfessionalEmployee и Teacher
    class Degree(Enum):
        BACHELOR = 'bachelor'
        SPECIALIST = 'specialist'
        MASTER = 'master'
        CANDIDATE = 'candidate'
        DOCTOR = 'doctor'

    def __init__(self,
                 # ДОБАВИТЬ: все параметры из каждого конструктора каждого родительского класса
                 courses: list[str],
                 professorship: bool):
        # ДОБАВИТЬ: вызов метода-конструктора родительского класса
        self.courses = courses
        self.professorship = professorship


class Student(Person):
    """Содержит информацию о студентах"""

    class EducationForm(Enum):
        INTRAMURAL = 'intramural'
        EXTRAMURAL = 'extramural'
        REMOTE = 'remote'

    class Contract(Enum):
        BUDGET = 'budget'
        COMPANY = 'company'
        PERSONAL = 'personal'

    def __init__(self,
                 # ДОБАВИТЬ: все параметры из каждого конструктора каждого родительского класса
                 form: EducationForm,
                 contract: Contract,
                 year: int,
                 speciality: str,
                 grant: Decimal):
        self.grant = grant
        self.speciality = speciality
        self.year = year
        self.contract = contract
        self.form = form
        # ИСПРАВИТЬ: перенести вызов super().__init__() в начало конструктора
        super().__init__(surname, name, patronymic, birthdate, gender, contact)


class OrganizationLevel(ABC):
    """Определяет структуру головной и дочерних организаций"""

    def __init__(self,
                 __budgets: dict[int, Decimal],
                 name: str,
                 __employees: list[Employee],
                 _head: Administrator,
                 contact: Contact,
                 __budget: Decimal):
        self.__budgets = __budgets
        self.name = name
        self.__employees = __employees
        self._head = _head
        self.contact = contact
        self.__budget = __budget

    # ДОБАВИТЬ: реализации для методов ниже

    def hire_employee(self) -> Employee:
        pass

    def fire_employee(self):
        pass

    def change_head(self):
        pass

    def set_budget(self):
        pass


class University(OrganizationLevel):
    """Содержит информацию о входящих в университет институтах и закрепленных за ними общежитиях"""

    def __init__(self,
                 # ДОБАВИТЬ: все параметры из конструктора родительского класса
                 institutes: list[Institute],
                 dormitories: list[Dormitory]):
        self.institutes = institutes
        self.dormitories = dormitories
        # ИСПРАВИТЬ: перенести вызов super().__init__() в начало конструктора
        super().__init__(__budgets, name, __employees, _head, contact, __budget)


class Dormitory(OrganizationLevel):
    """Содержит информацию о комнатах в общежитиях и проживающих в них студентах"""

    def __init__(self,
                 # ДОБАВИТЬ: все параметры из конструктора родительского класса
                 __rooms: dict[str, list[Student]]):
        self.__rooms = __rooms
        # ИСПРАВИТЬ: перенести вызов super().__init__() в начало конструктора
        super().__init__(__budgets, name, __employees, _head, contact, __budget)

    # ДОБАВИТЬ: реализации для метода ниже

    def checkin_student(self,
                        room_number: str,
                        student: Student):
        pass


class Institute(OrganizationLevel):
    """Содержит информацию о факультетах в институте и их деканах"""

    # ДОБАВИТЬ: все параметры из конструктора родительского класса
    def __init__(self, departments: list[Department]):
        self.departments = departments
        # ИСПРАВИТЬ: перенести вызов super().__init__() в начало конструктора
        super().__init__(__budgets, name, __employees, _head, contact, __budget)

    # ДОБАВИТЬ: реализации для метода ниже

    def change_head(self):
        pass


class Department(OrganizationLevel):
    """Содержит информацию о факультетах в институте и их деканах"""

    def __init__(self,
                 # ДОБАВИТЬ: все параметры из конструктора родительского класса
                 groups: list[Group]):
        self.groups = groups
        # ИСПРАВИТЬ: перенести вызов super().__init__() в начало конструктора
        super().__init__(__budgets, name, __employees, _head, contact, __budget)

    # ДОБАВИТЬ: реализации для методов ниже

    def change_head(self):
        pass

    def add_group(self):
        pass

    def remove_group(self):
        pass


class Group(list):
    """Содержит информацию о группах, старостах, кураторах"""

    def __init__(self,
                 name: str,
                 chief: Student,
                 curator: Teacher):
        # КОММЕНТАРИЙ: наследование от встроенного класса ничем не отличается от наследования от пользовательского класса с точки зрения порядка, в котором целесообразно производить расширение конструктора — этот пример и должен был подсказать вам нужный порядок
        # КОММЕНТАРИЙ: я не могу на лекциях рассказать абсолютно обо всём, иначе мне пришлось бы говорить несколько суток подряд по каждой теме — учитесь извлекать подсказки для себя отовсюду
        super().__init__()
        self.name = name
        self.chief = chief
        self.curator = curator

    # ДОБАВИТЬ: реализации для методов ниже

    def change_chief(self):
        pass

    def change_curator(self):
        pass


# ИТОГ: довольно халатно для вас, задача требует серьёзной доработки — 4/12


# СДЕЛАТЬ: вторая задача довольно тесно связана с первой: попытавшись поработать с экземплярами определённых вами классов вы смогли бы самостоятельно прийти к ряду выводов о том, как удобнее объявлять классы
