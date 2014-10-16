class Panda:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def _get_fatter(self):
        if self.weight < 1000:
            self.weight += 1

    def eat(self):
        self._get_fatter()
        print("Nomm nomm nomm! Bamboo.")


class KungFuPanda(Panda):

    def __init__(self, name, age, weight, skill):
        super().__init__(name, age, weight)
        self.skill = skill

    def fight(self):
        self.weight -= 1
        print("Bam bam!")


po = Panda("Po", 5, 700)
po.eat() # Nomm nomm nomm! Bamboo.
