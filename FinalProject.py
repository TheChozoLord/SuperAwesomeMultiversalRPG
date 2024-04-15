# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 09:09:56 2024

@author: owen.merrill
"""
import pygame, random, simpleGE

class Characters(simpleGE.Sprite):
    def __init__(self, 
                 scene, 
                 HP = 0,
                 attack = 0,
                 dodge = 0):
        super().__init__(scene)
        
        self.HP = HP
        self.attack = attack
        self.dodge = dodge
        self.name = "Sonic"
        
        self.image = (pygame.image.load("sonicWPlaceholder.png"))
        self.setSize(50, 75)
        self.position = (320, 400)
        
class Enemies(simpleGE.Sprite):
    def __init__(self, 
                 scene, 
                 HP = 0,
                 attack = 0,
                 dodge = 0):
        super().__init__(scene)
        
        self.HP = HP
        self.attack = attack
        self.dodge = dodge
        
        def attack(self, target):
            hit = random.randint(1,100)
            if (hit >= target.dodge):
                damage = random.randint(1, self.attack)
                target.health -= damage
                print(f"""{self.name} deals {damage} points of damage to {target.name}.""")
            else:
                print(f"""{self.name} misses.""")
        
        self.image = (pygame.image.load("skelenemy.jpg"))
        self.setSize(50, 75)
        self.position = (120, 400)
        
class BattleScene(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("white.jpg")
        
        self.Characters = Characters(self)
        self.Enemies = Enemies(self)
        
        self.lblsonichealth = simpleGE.Label(f"{self.character.health}")
        
        def process(self):
            self.fight()
            self.Enemies(self.attack)
        
        def fight(self):
            keepGoing = True
            while keepGoing == True:
                print(f"""{self.Character.name}: {self.Character.health}""")
                print(f"""{self.Enemies.name}: {self.Enemies.health}""")
                input("press enter to attack.")
                self.Characters.attack(self.Enemies)
                self.Enemies.attack(self.Characters)
                if self.Character.health <= 0:
                    print("You lose.")
                    keepGoing = False
                if self.Enemies.health <= 0:
                    print("You win!")
                    keepGoing = False
        
        self.sprites = [self.Characters,
                        self.Enemies,
                        self.lblsonichealth]
        
def main():
    battle = BattleScene()
    battle.start()
        
if __name__ == "__main__":
    main()