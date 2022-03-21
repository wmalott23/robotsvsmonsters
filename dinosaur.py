class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = int(attack_power)
        self.health = 50

    def attack(self, robot):
        print(f'{self.name} attacks {robot.name} with a big stomp and does {self.attack_power} points of damage!')
