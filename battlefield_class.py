from robot_class import Robot
from dinosaur_class import Dinosaur

class Battlefield:
    def __init__(self):
        robot = Robot('R2D2')
        dinosaur = Dinosaur('T-Rex', 20)
        self.robot = robot
        self.dinosaur = dinosaur

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print(f'Welcome to Robots vs Dinosaurs!')
        print(f'Battlefield loaded!')
        print(f'Robot: {self.robot.name}')
        print(f'Dinosaur: {self.dinosaur.name}')

    def battle_phase(self):
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.dinosaur.attack(self.robot)
            if self.robot.health <= 0:
                break
            Robot.choose_weapon(self.robot) # choose weapon before attacking
            self.robot.attack(self.dinosaur)
            if self.dinosaur.health <= 0:
                break

# as a developer, I want the battle to conclude once either the robot or the dinosaur has its health points reduced to zero
    def display_winner(self):
        if self.robot.health <= 0:
            print(f'{self.dinosaur.name} is the winner!')
        elif self.dinosaur.health <= 0:
            print(f'{self.robot.name} is the winner!')
        else:
            print(f'Both {self.robot.name} and {self.dinosaur.name} have died!')

#