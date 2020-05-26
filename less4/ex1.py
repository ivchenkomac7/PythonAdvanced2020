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

    def __init__(self, surname, birthday, faculty):
        self.surname = surname
        self.birthday = birthday
        self.faculty = faculty

    @abc.abstractmethod
    def person_info(self):
        pass

    @abc.abstractmethod
    def person_age(self):
        birthday = datetime.datetime.strptime(self.birthday, '%Y, %m, %d')
        now_date = datetime.date.today()
        age = now_date.year - birthday.year
        if now_date.month < birthday.month:
            age -= 1
        elif now_date.month == birthday.month and now_date.day < birthday.day:
            age -= 1
        return age


class Abiturient(AbstractPerson):

    @property
    def person_info(self):
        return self.surname, self.birthday, self.faculty
    
    def person_age(self):
        super().person_age()


class Student(AbstractPerson):

    def __init__(self, surname, birthday, faculty, course):
        AbstractPerson.__init__(self, surname, birthday, faculty)
        self.course = course

    @property
    def person_info(self):
        return Abiturient.person_info, self.course

    def person_age(self):
        super().person_age()


y = Student('AAA', '1987, 7, 31', 'asd', 2)


x = Abiturient('AAA', '1986, 7, 31', 'asd')

print(x.person_info)
print(x.person_age())
print(y.person_info)
print(y.person_age())
