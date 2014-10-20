class Orc(Entity):

    def __init__(self, name, health,berserk_factor):
        super().__init__(name, health)
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
