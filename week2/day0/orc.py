class Orc:

    def __init__(self,name,health,berserk_factor):
        self.name = name
        self.maxhealth = health
        self.berserk_factor = berserk_factor


    def berserk_factor_check(self):
        if self.berserk_factor < 1:
            self.berserk_factor = 1
            return self.berserk_factor

        elif self.berserk_factor > 2:
            self.berserk_factor = 2
            return self.berserk_factor

        else:
            return self.berserk_factor

    def get_health(self):
        return self.maxhealth

    def is_alive(self):
        if self.maxhealth > 0:
            return True
        return False

    def take_damage(self,damage_points):
        if damage_points > self.maxhealth:
            self.maxhealth = 0
            return self.maxhealth
        else:
            return self.maxhealth - damage_points

    def take_healing(self,healing_points):
        if self.maxhealth == 0:
            return False
        elif self.maxhealth + healing_points > 100:
            return False
        elif self.maxhealth + healing_points < 100:
            return True


