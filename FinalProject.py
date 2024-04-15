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
        
        self.image = (pygame.image.load("sonicWPlaceholder.png"))
        self.setSize(50, 75)
        self.position = (320, 400)
        
class Enemies(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        
        self.image = (pygame.image.load("skelenemy.jpg"))
        self.setSize(50, 75)
        self.position = (120, 400)
        
class BattleScene(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("white.jpg")
        
        self.Characters = Characters(self)
        self.Enemies = Enemies(self)
        
        self.sprites = [self.Characters,
                        self.Enemies]
        
def main():
    battle = BattleScene()
    battle.start()
        
if __name__ == "__main__":
    main()