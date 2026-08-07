from abc import ABC, abstractmethod
from exceptions import InvalidRatingError, NegativeDistanceError

class Vehicle(ABC):

    def __init__(self, driver_name, rating, distance):
        self.driver_name = driver_name
        self.rating = rating
        self.distance = distance

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if value < 1 or value > 5:
            raise InvalidRatingError("Rating must be between 1 and 5.")
        self.__rating = value

    @abstractmethod
    def calculate_fare(self):
        pass

class Bike(Vehicle):

    def calculate_fare(self):
        if self.distance < 0:
            raise NegativeDistanceError("Distance cannot be negative.")
        return self.distance * 15

class Car(Vehicle):

    def calculate_fare(self):
        if self.distance < 0:
            raise NegativeDistanceError("Distance cannot be negative.")
        return self.distance * 25