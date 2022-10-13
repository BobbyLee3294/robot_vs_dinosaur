# as a developer, I want to create a class named Robot that has the following attributes:
# name
# health
# attack_power
# weapon from weapon_class.py
from weapon_class import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.power_level = 100
        self.weapon = Weapon('Flamethrower', 30)
        self.active_weapon = self.weapon

# as a developer, I want a Robot to have the the ability to attack a dinosaur on the battlefield
# this attack method should lower a dinosaur's health by the attack_power of the robot's active weapon
    def attack(self, dinosaur):
        print(f'{self.name} attacked {dinosaur.name} with its {self.active_weapon.name} for {self.active_weapon.attack_power} damage!')
        dinosaur.health -= self.active_weapon.attack_power
        print(f'{dinosaur.name} has {dinosaur.health} health remaining.')

# as a developer, I want to choose from a list in weapon_class.py to assign a weapon to the robot
    def choose_weapon(self):
        weapon_list = ['Flamethrower', 'Laser', 'Missile']
        print(f'Choose a weapon for {self.name}!')
        for index, weapon in enumerate(weapon_list):
            print(f'{index+1}. {weapon}')
        weapon_choice = int(input('Enter a number: '))
        if weapon_choice == 1:
            self.active_weapon = Weapon('Flamethrower', 30)
        elif weapon_choice == 2:
            self.active_weapon = Weapon('Laser', 40)
        elif weapon_choice == 3:
            self.active_weapon = Weapon('Missile', 50)
        else:
            print('Invalid input. Please try again.')
            self.choose_weapon()