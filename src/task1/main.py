# Наступний код представляє просту систему для створення транспортних засобів. У нас є два класи: Car та Motorcycle. Кожен клас має метод start_engine(), який імітує запуск двигуна відповідного транспортного засобу. Наразі, щоб створити новий транспортний засіб, ми просто створюємо екземпляр відповідного класу з вказаними маркою (make) та моделлю (model).
# Наступним кроком потрібно створювати транспортні засоби з урахуванням специфікацій різних регіонів наприклад, для США US Spec та ЄС EU Spec.
# Ваше завдання — реалізувати патерн фабрика, який дозволить створювати транспортні засоби з різними регіональними специфікаціями, не змінюючи основні класи транспортних засобів.
# Ход виконання завдання 1:
# Створити абстрактний базовий клас Vehicle з методом start_engine().
# Змінити класи Car та Motorcycle, щоб вони успадковувались від Vehicle.
# Створити абстрактний клас VehicleFactory з методами create_car() та create_motorcycle().
# Реалізувати два класи фабрики: USVehicleFactory та EUVehicleFactory. Ці фабрики повинні створювати автомобілі та мотоцикли з позначкою регіону наприклад, Ford Mustang (US Spec) відповідно для США.
# Змініть початковий код так, щоб він використовував фабрики для створення транспортних засобів.
from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class Vehicle(ABC):
    def __init__(self, make, model, region):
        self.make = make
        self.model = model
        self.region = region

    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        print(f"{self.make} {self.model} ({self.region}): Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        print(f"{self.make} {self.model} ({self.region}): Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model) -> Car:
        return Car(make=make, model=model, region="US Spec")

    def create_motorcycle(self, make, model) -> Motorcycle:
        return Motorcycle(make=make, model=model, region="US Spec")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model) -> Car:
        return Car(make=make, model=model, region="EU Spec")

    def create_motorcycle(self, make, model) -> Motorcycle:
        return Motorcycle(make=make, model=model, region="EU Spec")


# Використання
eu_factory = EUVehicleFactory()
vehicle1 = eu_factory.create_car(make="Toyota", model="Corolla")
vehicle1.start_engine()

vehicle2 = eu_factory.create_motorcycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()

us_factory = USVehicleFactory()
vehicle3 = us_factory.create_car("Toyota", "Corolla")
vehicle3.start_engine()

vehicle4 = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
vehicle4.start_engine()
