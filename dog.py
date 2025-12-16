class Dog:
    def __init__(self, name: str, age: int, gender: str, size: str):
        self.name = name
        self.age = age
        self.gender = gender
        self.health = int
        self.strength = int
        self.agility = int
        # initializing grandparent class, Dog
    def bark(self) -> str:
        return self.name + 'barked at the opponent, Woof woof!'
    
    def run_away(self) -> str:
        return self.name + 'ran away from the fight!'
    
    def eat(self, food_effect: dict) -> str:
        if 'health' in food_effect:
            self.health += food_effect['health']
            return self.name + 's health rose! New health stat:' + self.health
        if 'strength' in food_effect:
            self.strength += food_effect['strength']
            return self.name + 's strength rose! New strength stat:' + self.strength
        if 'agility' in food_effect:
            self.agility += food_effect['agility']
            return self.name + 's agility rose! New agility stat:' + self.agility
        
        self.health = min(0, self.health)
        self.strength = min(0, self.strength)
        self.agility = min(0, self.agility)

    def faint(self) -> str:
        if self.health == 0 or self.strength == 0:
            return self.name + 'cannot fight! They have fainted!'
        
    def pant(self) -> str:
        if self.agility == 0:
            return self.name + 'is tired. They pant to gain some energy'
        self.agility += 1