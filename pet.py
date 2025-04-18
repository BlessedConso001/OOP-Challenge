
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        # TODO
        self.hunger = max (0, self.hunger-3)
        self.happiness += 1
        print(f'{self.name} is hunger is {self.hunger} and happines is {self.happiness}')
    def sleep(self):
        #self.eat()
        # TODO
        self.energy = min(10, self.energy + 5)
        print(f'energy is{self.energy}')
    def play(self):
        #self.sleep()
        # TODO
        #decreases energy by 2, increases happiness by 2, and increases hunger by 1.
        self.energy -= 2
        self.happiness += 2
        self.hunger += 1
        print(f'{self.name} has currently energy of {self.energy} and hapiness level of {self.happiness} and hunger level of {self.hunger}')
    def train(self, trick):
        # TODO
        self.tricks.append(trick)
    def show_tricks(self):
        # TODO
        print(f"Display tricks{self.tricks}")
    def get_status(self):
        # TODO
        print(f'My Pet {self.name} with hunger level of {self.hunger} and energy of {self.energy} and happiness of {self.happiness}\n these are the tricks {self.tricks}')



