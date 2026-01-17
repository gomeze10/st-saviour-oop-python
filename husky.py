from work import WorkingDogs
from stats import Stats

class SiberianHusky(WorkingDogs):
    def __init__(self, age, gender, name):
        super().__init__(age, gender, name, "Siberian Husky", "Large", 8)

        # 👇 child-specific stats
        self.stats = Stats(
            attack=6,
            defense=7,
            health=9
        )

    def pull_sled(self):
        return f"{self.name} is pulling a sled."
