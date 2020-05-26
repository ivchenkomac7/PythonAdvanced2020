# Создайте класс ПЕРСОНА с абстрактными методами, позволяющими
# вывести на экран информацию о персоне, а также определить ее возраст (в
# текущем году). Создайте дочерние классы: АБИТУРИЕНТ (фамилия, дата
# рождения, факультет), СТУДЕНТ (фамилия, дата рождения, факультет, курс),
# ПРЕПОДАВАТЕЛЬ (фамилия, дата рождения, факультет, должность, стаж),
# со своими методами вывода информации на экран и определения возраста.
# Создайте список из n персон, выведите полную информацию из базы на
# экран, а также организуйте поиск персон, чей возраст попадает в заданный
# диапазон.


import abc
import datetime


class AbstractPerson(abc.ABC):

    @abc.abstractmethod
    def __init__(self, surname, birthday, faculty):
        self.surname = surname
        self.birthday = birthday
        self.faculty = faculty

    @abc.abstractmethod
    def person_info(self):
        return f'Surname: {self.surname}, BD: {self.birthday}, Faculty: {self.faculty}'

    @abc.abstractmethod
    def person_age(self):
        birthday = datetime.datetime.strptime(self.birthday, '%Y/%m/%d')
        now_date = datetime.date.today()
        age = now_date.year - birthday.year
        if now_date.month < birthday.month:
            age -= 1
        elif now_date.month == birthday.month and now_date.day < birthday.day:
            age -= 1
        return age


class Abiturient(AbstractPerson):

    def __init__(self, surname, birthday, faculty):
        super().__init__(surname, birthday, faculty)

    @property
    def person_info(self):
        return super().person_info()

    @property
    def person_age(self):
        return super().person_age()


class Student(AbstractPerson):

    def __init__(self, surname, birthday, faculty, course):
        super().__init__(surname, birthday, faculty)
        self.course = course

    @property
    def person_info(self):
        return f'{super().person_info()}, Course: {self.course}'

    @property
    def person_age(self):
        return super().person_age()


class Teacher(AbstractPerson):

    def __init__(self, surname, birthday, faculty, position, experience):
        super().__init__(surname, birthday, faculty)
        self.position = position
        self.experience = experience

    @property
    def person_info(self):
        return f'{super().person_info()}, Position: {self.position}, Experience: {self.experience}'

    @property
    def person_age(self):
        return super().person_age()


ab = Abiturient('Mask', '1986/7/31', 'IT')

st = Student('Zuckerberg', '1987/10/3', 'Electronics', 2)

tch = Teacher('Gates', '1980/4/25', 'IT', 'Teacher', 10)

persons_list = [ab, st, tch]

for i in persons_list:
    print(i.person_info)

for i in persons_list:
    if int(i.person_age) > 32:
        print(f'{i.surname} over 35 year old')

# print(ab.surname)
# print(ab.person_age())
# print(st.person_info)
# print(st.person_age())
# print(tch.person_info)
# print(tch.person_age())
