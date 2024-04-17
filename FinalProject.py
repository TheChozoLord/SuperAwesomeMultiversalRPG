# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 09:09:56 2024

@author: owen.merrill
"""
import time, pygame, random, simpleGE

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
        self.position = (500, 400)
        
    def attack(self, target):
        print("Sonic Attacks")
        hit = random.randint(1,100)
        if (hit >= target.dodge):
            damage = random.randint(1, self.atk)
            target.HP -= damage
            print(f"""{self.name} deals {damage} points of damage to {target.name}.""")
        else:
            print(f"""{self.name} misses.""")
    
    def SPattack(self, target):
        print("Sonic uses his Special Attack")
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
                 HP = 10,
                 atk = 1,
                 dodge = 20):
        super().__init__(scene)
        
        self.HP = HP
        self.atk = atk
        self.dodge = dodge
        self.name = "Skeley"
        
        self.image = (pygame.image.load("skelenemy.jpg"))
        self.setSize(50, 75)
        self.position = (120, 400)
        
    def attack(self, target):
        print("Skeley attacks")
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
        
        self.outcome = 0
        
        self.Characters = Characters(self)
        self.Enemies = Enemies(self)
        
        self.lblsonichealth = simpleGE.Label()
        self.lblsonichealth.text = (f"{self.Characters.name} HP: {self.Characters.HP}")
        self.lblsonichealth.center = (500, 100)
        
        self.lblenemyhealth = simpleGE.Label()
        self.lblenemyhealth.text = (f"{self.Enemies.name} HP: {self.Enemies.HP}")
        self.lblenemyhealth.center = (100, 100)
        
        self.lblfeed = simpleGE.Label()
        self.lblfeed.text = ("Battle Start!")
        self.lblfeed.center = (300, 50)
        self.lblfeed.size = (300, 40)
        
        self.sprites = [self.Characters,
                        self.Enemies,
                        self.lblsonichealth,
                        self.lblenemyhealth,
                        self.lblfeed]
        
    def processEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key ==  pygame.K_a:
                self.lblfeed.text = (f"{self.Characters.name} attacks {self.Enemies.name}")
                self.Characters.attack(self.Enemies)
                self.lblenemyhealth.text = (f"{self.Enemies.name} HP: {self.Enemies.HP}")
                self.enemyAttacks()
            if event.key ==  pygame.K_s:
                self.lblfeed.text = (f"{self.Characters.name} uses spcial attack on {self.Enemies.name}")
                self.Characters.SPattack(self.Enemies)
                self.lblenemyhealth.text = (f"{self.Enemies.name} HP: {self.Enemies.HP}")
                self.enemyAttacks()
            #self.enemyAttacks()
            
    def enemyAttacks(self):
        #time.sleep(3)
        self.lblfeed.text = (f"{self.Enemies.name} attacks {self.Characters.name}")
        self.Enemies.attack(self.Characters)
        self.lblsonichealth.text = (f"{self.Characters.name} HP: {self.Characters.HP}")
                
    def process(self):
        if self.Characters.HP <= 0:
            print("You lose")
            self.outcome = 1
            self.stop()
        if self.Enemies.HP <= 0:
            print("You win")
            self.outcome = 2
            self.stop()

class TitleScreen(simpleGE.Scene):
    def __init__(self, outcome):
        super().__init__()
        self.setImage("white.jpg")
        
        self.response = "P"
        
        self.instructions = simpleGE.MultiLabel()
        self.instructions.textLines = [
            "Defeat your enemy.",
            "Press a to attack.",
            "Press s to use a special attack.",
            "Good luck."
            ]
        
        self.instructions.center = (320, 240)
        self.instructions.size = (500, 250)
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Play (up)"
        self.btnPlay.center = (100, 400)
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit (down)"
        self.btnQuit.center = (550, 400)
        
        self.outcome = outcome
        
        
        self.sprites = [self.instructions,
                        self.btnPlay,
                        self.btnQuit]
                
    def process(self):
        if self.outcome == 1:
            self.instructions.textLines = [
                "You Lost.",
                "Press a to attack.",
                "Press s to use a special attack.",
                "Good luck."
                ]
        if self.outcome == 2:
            self.instructions.textLines = [
                "You Won!",
                "Press a to attack.",
                "Press s to use a special attack.",
                "Good luck."
                ]
        if self.isKeyPressed(pygame.K_UP):
            self.response = "Play"
            self.stop()
        if self.isKeyPressed(pygame.K_DOWN):
            self.response = "Quit"
            self.stop()        
        
def main():
    keepGoing = True
    outcome = 0
    while keepGoing:
        instructions = TitleScreen(outcome)
        instructions.start()
        if instructions.response == "Play":
            battle = BattleScene()
            battle.start()
            outcome = battle.outcome
        else:
            keepGoing = False
        
if __name__ == "__main__":
    main()