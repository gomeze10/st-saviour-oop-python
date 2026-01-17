from dog import Dogs

class WorkingDogs(Dogs):
    def __init__(self, age, gender, name, breed, size, strength_level):
        super().__init__(age, gender, name, breed, size)
        self.strength_level = strength_level

    def protect(self):
        return f"{self.name} is protecting."

    def speak(self):
        return "Bark!"


