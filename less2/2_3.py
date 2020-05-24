# Создать класс точки, реализовать конструктор который
# инициализирует 3 координаты (Class): Определенный программистом тип данных.x, y, z). Реалзиовать методы для ). Реалзиовать методы для
# получения и изменения каждой из координат. Перегрузить для этого
# класса методы сложения, вычитания, деления умножения.
# Перегрузить один любой унарный метод.
# Ожидаемый результат: умножаю точку с координатами 1,2,3 на
# другую точку с такими же координатами, получаю результат 1, 4, 9.


class Dot:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Dot(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Dot(self.x - other.x, self.y - other.y, self.z - other.z)

    def __truediv__(self, other):
        return Dot(self.x / other.x, self.y / other.y, self.z / other.z)

    def __mul__(self, other):
        return Dot(self.x * other.x, self.y * other.y, self.z * other.z)

    def __neg__(self):
        return Dot(-self.x, -self.y, -self.z)

    def __str__(self):
        return f'{self.x}, {self.y}, {self.z}'


d1 = Dot(10, 20, 30)
d2 = Dot(20, 30, 40)

result1 = d1 + d2
result2 = d1 - d2
result3 = d1 / d2
result4 = d1 * d2
result5 = -d1

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)


