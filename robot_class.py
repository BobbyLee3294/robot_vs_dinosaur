from weapon_class import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.power_level = 100
        self.weapon = Weapon('Flamethrower', 30)
        self.active_weapon = self.weapon

    def attack(self, dinosaur):
        print(f'{self.name} attacked {dinosaur.name} with its {self.active_weapon.name} for {self.active_weapon.attack_power} damage!')
        dinosaur.health -= self.active_weapon.attack_power
        print(f'{dinosaur.name} has {dinosaur.health} health remaining.')