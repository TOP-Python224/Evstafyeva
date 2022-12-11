from abc import ABC
from dataclasses import dataclass
from decimal import Decimal
from datetime import date
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
                 _prev_experience: int,
                 salary: Decimal,
                 position: str,
                 head: Administrator,
                 surname: str,
                 name: str,
                 patronymic: str,
                 birthdate: date,
                 gender: Gender,
                 contact: Contact):
        self.hire_date = hire_date
        self.prev_experience = prev_experience
        self.salary = salary
        self.position = position
        self.head = head

        super().__init__(surname, name, patronymic, birthdate, gender, contact)

    @property
    def experience(self):
        return None

class Administrator(Employee):

    def __init__(self,
                 division: str,
                 subordinates: list[Employee]):

        self.subordinates = subordinates
        self.division = division

        super().__init__(hire_date,
                         _prev_experience,
                         salary, position,
                         head, surname,
                         name, patronymic,
                         birthdate,
                         gender, contact)



class ProfessionalEmployee(Employee):
    """Содержит информацию об ученой степени и званиях профессорско-преподавательского состава"""

    def __init__(self, degree: Degree):
        self.degree = degree

        super().__init__(hire_date,
                         _prev_experience,
                         salary, position,
                         head, surname,
                         name, patronymic,
                         birthdate,
                         gender, contact)


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
                 institutes: list[Institute],
                 dormitories: list[Dormitory]):
        self.institutes = institutes
        self.dormitories = dormitories

        super().__init__(__budgets, name, __employees, _head, contact, __budget)


class Dormitory(OrganizationLevel):
    """Содержит информацию о комнатах в общежитиях и проживающих в них студентах"""

    def __init__(self,
                 __rooms: dict[str, list[Student]]):
        self.__rooms = __rooms

        super().__init__(__budgets, name, __employees, _head, contact, __budget)

    def checkin_student(self,
                        room_number: str,
                        student: Student):
        pass


class Institute(OrganizationLevel):
    """Содержит информацию о факультетах в институте и их деканах"""

    def __init__(self, departments: list[Department]):
        self.departments = departments

        super().__init__(__budgets, name, __employees, _head, contact, __budget)

    def change_head(self):
        pass


class Department(OrganizationLevel):
    """Содержит информацию о факультетах в институте и их деканах"""

    def __init__(self,
                 groups: list[Group]):
        self.groups = groups

        super().__init__(__budgets, name, __employees, _head, contact, __budget)

    def change_head(self):
        pass

    def add_group(self):
        pass

    def remove_group(self):
        pass


class Group(list):
    """Содержит информацию о группах, ствростах, кураторах"""

    def __init__(self,
                 name: str,
                 chief: Student,
                 curator: Teacher):
        super().__init__()
        self.name = name
        self.chief = chief
        self.curator = curator

    def change_chief(self):
        pass

    def change_curator(self):
        pass


class Student(Person):
    """Содержит информацию о cтудентах"""

    class EducationForm(Enum):
        INTRAMURAL = 'intramural'
        EXTRAMURAL = 'extramural'
        REMOTE = 'remote'

    class Contract(Enum):
        BUDGET = 'budget'
        COMPANY = 'company'
        PERSONAL = 'personal'

    def __init__(self,
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

        super().__init__(surname, name, patronymic, birthdate, gender, contact)


class Teacher(ProfessionalEmployee):
    """Содержит информацию о преподавателях и курсах, которые они ведут"""

    class Degree(Enum):
        BACHELOR = 'bachelor'
        SPECIALIST = 'specialist'
        MASTER = 'master'
        CANDIDATE = 'candidate'
        DOCTOR = 'doctor'

    def __init__(self,
                 courses: list[str],
                 professorship: bool,
                 ):
        self.courses = courses
        self.professorship = professorship


class Researcher(ProfessionalEmployee):
    pass


class GeneralPersonnel(Employee):
    pass



