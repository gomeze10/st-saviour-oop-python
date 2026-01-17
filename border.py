from herd import HerdingGroup
from stats import Stats

class BorderCollie(HerdingGroup):
    def __init__(self, age, gender, name):
        super().__init__(age, gender, name, "Border Collie", "Medium", True)

        # 👇 child-specific stats
        self.stats = Stats(
            attack=7,
            defense=5,
            health=8
        )

    def quick_turn(self):
        return f"{self.name} makes a quick turn."

