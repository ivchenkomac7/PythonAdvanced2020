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
        pass


class Abiturient(AbstractPerson):

    # def __init__(self, surname, birthday, faculty):
    #     self.surname = surname
    #     self.birthday = birthday
    #     self.faculty = faculty

    @property
    def person_info(self):
        return self.surname, self.birthday, self.faculty

    @property
    def person_age(self):
        birthday = datetime.datetime.strptime(self.birthday, '%Y, %m, %d')
        now_date = datetime.date.today()
        age = now_date.year - birthday.year
        if now_date.month < birthday.month:
            age -= 1
        elif now_date.month == birthday.month and now_date.day < birthday.day:
            age -= 1
        return age


class Student(AbstractPerson):

    def __init__(self, surname, birthday, faculty, course):
        AbstractPerson.__init__(self, surname, birthday, faculty)
        self.course = course

    @property
    def person_info(self):
        return Abiturient.person_info, self.course

    @property
    def person_age(self):
        birthday = datetime.datetime.strptime(self.birthday, '%Y, %m, %d')
        now_date = datetime.date.today()
        age = now_date.year - birthday.year
        if now_date.month < birthday.month:
            age -= 1
        elif now_date.month == birthday.month and now_date.day < birthday.day:
            age -= 1
        return age


y = Student('AAA', '1987, 7, 31', 'asd', 2)


x = Abiturient('AAA', '1986, 7, 31', 'asd')
print(y.person_info)
print(y.person_age)
