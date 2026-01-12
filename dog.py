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


# making Parent Classes 

class HerdingGroup(Dogs):
    def __init__(self, age, gender, name, breed, size, herding_instinct):
        super().__init__(age, gender, name, breed, size)
        self.herding_instinct = herding_instinct

    def herd(self):
        return f"{self.name} is herding."

    def speak(self):
        return "Woof!"


class WorkingDogs(Dogs):
    def __init__(self, age, gender, name, breed, size, strength_level):
        super().__init__(age, gender, name, breed, size)
        self.strength_level = strength_level

    def protect(self):
        return f"{self.name} is protecting."

    def speak(self):
        return "Bark!"


# making Child Classes

class BorderCollie(HerdingGroup):
    def __init__(self, age, gender, name, speed):
        super().__init__(age, gender, name, "Border Collie", "Medium", True)
        self.speed = speed

    def quick_turn(self):
        return f"{self.name} makes a quick turn."

    def __repr__(self):
        return f"BorderCollie(name={self.name}, speed={self.speed})"


class SiberianHusky(WorkingDogs):
    def __init__(self, age, gender, name, cold_resistance):
        super().__init__(age, gender, name, "Siberian Husky", "Large", 8)
        self.cold_resistance = cold_resistance

    def pull_sled(self):
        return f"{self.name} is pulling a sled."

    def __repr__(self):
        return f"SiberianHusky(name={self.name}, cold_resistance={self.cold_resistance})"


# Variadic Function

def feed_dogs(*dogs):
    return [dog.eat() for dog in dogs]
