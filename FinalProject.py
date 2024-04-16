# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 09:09:56 2024

@author: owen.merrill
"""
import pygame, random, simpleGE

class Characters(simpleGE.Sprite):
    def __init__(self, 
                 scene, 
                 HP = 5,
                 atk = 5,
                 dodge = 60):
        super().__init__(scene)
        
        self.HP = HP
        self.atk = atk
        self.dodge = dodge
        self.name = "Sonic"
        
        self.image = (pygame.image.load("sonicWPlaceholder.png"))
        self.setSize(50, 75)
        self.position = (320, 400)
        
    def attack(self, target):
        print(f"""{target}""")
        hit = random.randint(1,100)
        if (hit >= target.dodge):
            damage = random.randint(1, self.atk)
            target.HP -= damage
            print(f"""{self.name} deals {damage} points of damage to {target.name}.""")
        else:
            print(f"""{self.name} misses.""")
        
class Enemies(simpleGE.Sprite):
    def __init__(self, 
                 scene, 
                 HP = 2,
                 atk = 1,
                 dodge = 20):
        super().__init__(scene)
        
        self.HP = HP
        self.atk = atk
        self.dodge = dodge
        self.name = "Skeley Boi"
        
        self.image = (pygame.image.load("skelenemy.jpg"))
        self.setSize(50, 75)
        self.position = (120, 400)
        
    def attack(self, target):
        hit = random.randint(1,100)
        if (hit >= target.dodge):
            damage = random.randint(1, self.atk)
            target.HP -= damage
            print(f"""{self.name} deals {damage} points of damage to {target.name}.""")
        else:
            print(f"""{self.name} misses.""")
        
        
        
class BattleScene(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("white.jpg")
        
        self.Characters = Characters(self)
        self.Enemies = Enemies(self)
        
        self.lblsonichealth = simpleGE.Label()
        self.lblsonichealth.text = (f"{self.Characters.HP}")
        self.lblsonichealth.center = (500, 100)
        
        self.sprites = [self.Characters,
                        self.Enemies,
                        self.lblsonichealth]
        
    def process(self):
        if self.isKeyPressed(pygame.K_a):
            print("Keypressed")
            self.fight()
        
    def fight(self):
        keepGoing = True
        while keepGoing == True:
            print(f"""{self.Characters.name}: {self.Characters.HP}""")
            print(f"""{self.Enemies.name}: {self.Enemies.HP}""")
            target = self.Enemies
            self.Characters.attack(target)
            target = self.Characters
            self.Enemies.attack(target)
            if self.Characters.HP <= 0:
                print("You lose.")
                keepGoing = False
            if self.Enemies.HP <= 0:
                print("You win!")
                keepGoing = False
        
def main():
    battle = BattleScene()
    battle.start()
        
if __name__ == "__main__":
    main()