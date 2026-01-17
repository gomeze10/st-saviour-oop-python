from dog import Dogs

class HerdingGroup(Dogs):
    def __init__(self, age, gender, name, breed, size, herding_instinct):
        super().__init__(age, gender, name, breed, size)
        self.herding_instinct = herding_instinct

    def herd(self):
        return f"{self.name} is herding."

    def speak(self):
        return "Woof!"