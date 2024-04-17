"""
Created on Mon Apr 15 09:09:56 2024

@author: owen.merrill
"""
import pygame, random, simpleGE

#def characters():
    #[name, HP, attack, dodge, MP, picture]
    #{Sonic: ["Sonic", 6, 7, 80, 16, sonicWPlaceholder.png]}
    #{Surge: ["Surge", 10, 10, 30, 12, Surge_Placeholder.png]}
    #{Three: ["Three", 4, 8, 75, 8, Agent_3_Placeholder.png]}
    
class characterSelect(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.image = (pygame.image.load("sonicWPlaceholder.png"))
        self.setSize(50, 75)
        self.position = (320, 50)

class Characters(simpleGE.Sprite):
    def __init__(self, 
                 scene, 
                 HP = 5,
                 atk = 5,
                 dodge = 60,
                 MP = 12,
                 name = "Sonic"):
        super().__init__(scene)
        
        characterDictionary ={
            1: ["Sonic", 6, 7, 80, 16, "sonicWPlaceholder.png"],
            2: ["Surge", 10, 10, 30, 12, "Surge_Placeholder.png"],
            3: ["Three", 4, 8, 75, 8, "Agent_3_Placeholder.png"]}
        
        self.HP = HP
        self.atk = atk
        self.dodge = dodge
        self.name = name
        self.spat = self.atk*2
        self.MP = MP
        
        self.image = (pygame.image.load("sonicWPlaceholder.png"))
        self.setSize(50, 75)
        self.position = (500, 400)
        
    def attack(self, target):
        hit = random.randint(1,100)
        if (hit >= target.dodge):
            damage = random.randint(1, self.atk)
            target.HP -= damage
    
    def SPattack(self, target):
        if (self.MP >= 4):
            self.enough = 1
            self.MP = self.MP - 4
            hit = random.randint(1,100)
            if (hit >= target.dodge):
                damage = random.randint(self.atk, self.spat)
                target.HP -= damage
        else:
            self.enough = 0

class Enemies(simpleGE.Sprite):
    def __init__(self, 
                 scene, 
                 HP = 30,
                 atk = 1,
                 dodge = 20):
        super().__init__(scene)
        
        self.HP = HP
        self.atk = atk
        self.dodge = dodge
        self.name = "Skeley"
        self.spat = self.atk*3
        
        self.image = (pygame.image.load("skelenemy.jpg"))
        self.setSize(50, 75)
        self.position = (120, 400)
        
    def attack(self, target):
        print ("Skeley attacks")
        ai = random.randint(1, 100)
        if (ai <= 85):
            hit = random.randint(1,100)
            if (hit >= target.dodge):
                damage = random.randint(1, self.atk)
                target.HP -= damage
        if (ai > 85):
            hit = random.randint(1,100)
            if (hit >= target.dodge):
                damage = random.randint(1, self.spat)
                target.HP -= damage  
        
class BattleScene(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("white.jpg")
        
        self.outcome = 0
        
        self.Characters = Characters(self)
        self.Enemies = Enemies(self)
        
        self.lblsonichealth = simpleGE.MultiLabel()
        self.lblsonichealth.textLines = [
            f"{self.Characters.name},",
            f"HP: {self.Characters.HP}",
            f"MP: {self.Characters.MP}"
                                         ]
        self.lblsonichealth.center = (500, 100)
        
        self.lblenemyhealth = simpleGE.Label()
        self.lblenemyhealth.text = (f"{self.Enemies.name} HP: {self.Enemies.HP}")
        self.lblenemyhealth.center = (100, 100)
        
        self.lblfeed = simpleGE.Label()
        self.lblfeed.text = ("Battle Start!")
        self.lblfeed.center = (300, 45)
        self.lblfeed.size = (300, 25)
        
        self.lblenemyactions = simpleGE.Label()
        self.lblenemyactions.text = ("Battle Start!")
        self.lblenemyactions.center = (300, 70)
        self.lblenemyactions.size = (300, 25)
        
        self.sprites = [self.Characters,
                        self.Enemies,
                        self.lblsonichealth,
                        self.lblenemyhealth,
                        self.lblfeed,
                        self.lblenemyactions]
        
    def processEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key ==  pygame.K_a:
                self.lblfeed.text = (f"{self.Characters.name} attacks {self.Enemies.name}")
                self.Characters.attack(self.Enemies)
                self.lblenemyhealth.text = (f"{self.Enemies.name} HP: {self.Enemies.HP}")
                self.enemyAttacks()
            if event.key ==  pygame.K_s:
                self.Characters.SPattack(self.Enemies)
                if self.Characters.enough == 1:
                    self.lblsonichealth.textLines = [
                        f"{self.Characters.name},",
                        f"HP: {self.Characters.HP}",
                        f"MP: {self.Characters.MP}"
                                                     ]
                    self.lblfeed.text = (f"{self.Characters.name} uses spcial attack on {self.Enemies.name}")
                if self.Characters.enough == 0:
                    self.lblfeed.text = ("You dont have enough MP")
                self.lblenemyhealth.text = (f"{self.Enemies.name} HP: {self.Enemies.HP}")
                self.enemyAttacks()
            
    def enemyAttacks(self):
        self.lblenemyactions.text = (f"{self.Enemies.name} attacks {self.Characters.name}")
        self.Enemies.attack(self.Characters)
        self.lblsonichealth.textLines = [
            f"{self.Characters.name},",
            f"HP: {self.Characters.HP}",
            f"MP: {self.Characters.MP}"
                                         ]
                
    def process(self):
        if self.Characters.HP <= 0:
            self.outcome = 1
            self.stop()
        if self.Enemies.HP <= 0:
            self.outcome = 2
            self.stop()

class TitleScreen(simpleGE.Scene):
    def __init__(self, outcome):
        super().__init__()
        self.setImage("white.jpg")
        
        self.charSelectSprite = characterSelect(self)
        
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
        
        self.charSelect = 1
        
        self.outcome = outcome
        
        self.sprites = [self.instructions,
                        self.btnPlay,
                        self.btnQuit,
                        self.charSelectSprite]
                
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
            
    def processEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if self.isKeyPressed(pygame.K_UP):
                self.response = "Play"
                self.stop()
            if self.isKeyPressed(pygame.K_DOWN):
                self.response = "Quit"
                self.stop()        
            if self.isKeyPressed(pygame.K_RIGHT):
                self.charSelect += 1
                if self.charSelect >= 4:
                    self.charSelect = 1
            if self.isKeyPressed(pygame.K_LEFT):
                self.charSelect -= 1
                if self.charSelect <= 0:
                    self.charSelect = 3
            if self.charSelect == 1:
                self.charSelectSprite.image = pygame.image.load("sonicWPlaceholder.png")
                self.charSelectSprite.setSize(50, 75)
                self.charSelectSprite.position = (320, 50)
            if self.charSelect == 2:
                self.charSelectSprite.image = pygame.image.load("Surge_Placeholder.png")
                self.charSelectSprite.setSize(50, 75)
                self.charSelectSprite.position = (320, 50)
            if self.charSelect == 3:
                self.charSelectSprite.image = pygame.image.load("Agent_3_Placeholder.png")
                self.charSelectSprite.setSize(50, 75)
                self.charSelectSprite.position = (320, 50)

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