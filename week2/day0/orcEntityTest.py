from entity import Entity

class Hero(Entity):

    def __init__(self, name, health, nickname):
        super().__init__(name, health)
        self.nickname = nickname
        self._MAX_HEALTH = self.health

    def known_as(self):
        return "{} the {}".format(self.name, self.nickname)

    def get_health(self):
        return self.health

    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def take_damage(self, damage_points):
        if self.health - damage_points < 0:
            self.health = 0
        else:
            self.health -= damage_points

    def take_healing(self, healing_points):

        if self.health == 0:
            return False

        if self._MAX_HEALTH < self.health + healing_points:
            self.health = self._MAX_HEALTH
            return True
        else:
            self.health += healing_points

        return True


