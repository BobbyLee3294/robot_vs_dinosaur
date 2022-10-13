# as a dveloper, I want to creat a class named Dinosaur that has the following attributes:
# name
# health
# attack_power
class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.attack_power = attack_power

# as a developer, I want a Dinosaur to have the the ability to attack a robot on the battlefield
# this attack method should lower a robot's health by the value of the dinosaur's attack_power
    def attack(self, robot):
        print(f'{self.name} attacked {robot.name} for {self.attack_power} damage!')
        robot.health -= self.attack_power
        print(f'{robot.name} has {robot.health} health remaining.')