class Stats:
    def __init__(self, attack, defense, health):
        self.attack = attack
        self.defense = defense
        self.health = health

    def __str__(self):
        return f"ATK:{self.attack} DEF:{self.defense} HP:{self.health}"

