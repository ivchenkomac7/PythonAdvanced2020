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
        return self.surname, self.birthday, self.faculty

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

    def __init__(self, surname, birthday, faculty):
        super().__init__(surname, birthday, faculty)

    @property
    def person_info(self):
        return super().person_info()
    
    def person_age(self):
        return super().person_age()


class Student(AbstractPerson):

    def __init__(self, surname, birthday, faculty, course):
        super().__init__(surname, birthday, faculty)
        self.course = course

    @property
    def person_info(self):
        return super().person_info(), self.course

    def person_age(self):
        return super().person_age()


class Teacher(AbstractPerson):

    def __init__(self, surname, birthday, faculty, position, experience):
        super().__init__(surname, birthday, faculty)
        self.position = position
        self.experience = experience

    @property
    def person_info(self):
        return super().person_info(), self.position, self.experience

    def person_age(self):
        return super().person_age()


x = Abiturient('AAA', '1986, 7, 31', 'it')

y = Student('AAA', '1987, 7, 31', 'communication', 2)

z = Teacher('BBB', '1980, 4, 25', 'it', 'Teacher', 10)


print(x.person_info)
print(x.person_age())
print(y.person_info)
print(y.person_age())
print(z.person_info)
print(z.person_age())
