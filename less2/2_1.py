# Создать класс автомобиля. Описать общие аттрибуты. Создать
# классы легкового автомобиля и грузового. Описать в основном
# классе базовые аттрибуты для автомобилей. Будет плюсом если в
# классах наследниках переопределите методы базового класса.


class Vehicle:

    description = "The class for vehicle"

    def __init__(self, model, vin):
        self._model = model
        self._vin = vin

    def get_model(self):
        return self._model

    def set_model(self, value):
        self._model = value

    def get_vin(self):
        return self._vin

    def set_vin(self, value):
        self._vin = value

    def move(self):
        print(f"{self._model} moving...")

    def __str__(self):
        return f"Model: {self._model}, vin: {self._vin}"


class Car(Vehicle):

    def headlights(self):
        print(f"Headlights of {self._model} are shine")

    def move(self):
        print(f"{self._model} moving faster")


class Truck(Vehicle):
    def trailer(self):
        print(f"{self._model} have a trailer")


car = Car("Ford", "zxc127625")

truck = Truck("Iveco", "QW124ert")

print(car)
car.move()
car.headlights()

print(truck)
truck.move()
truck.trailer()
