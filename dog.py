from abc import ABC, abstractmethod

class Dogs(ABC):
    def __init__(self, age, gender, name, breed, size):
        self.age = age
        self.gender = gender
        self.name = name
        self.breed = breed
        self.size = size

    @abstractmethod
    def speak(self):
        pass

    def walk(self):
        return f"{self.name} is walking."

    def eat(self):
        return f"{self.name} is eating."

    def __str__(self):
        return f"{self.name} the {self.breed} ({self.size})"





