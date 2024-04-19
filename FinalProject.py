"""
Created on Mon Apr 15 09:09:56 2024

@author: owen.merrill
"""
import pygame, random, simpleGE
    
class characterSelect(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.image = (pygame.image.load("sonicWPlaceholder.png"))
        self.setSize(50, 75)
        self.position = (320, 50)

class Character(simpleGE.Sprite):
    def __init__(self, 
                 scene, 
                 characterInfo):
        super().__init__(scene)
        
        self.HP = characterInfo[1]
        self.atk = characterInfo[2]
        self.dodge = characterInfo[3]
        self.name = characterInfo[0]
        self.spat = self.atk*2
        self.MP = characterInfo[4]
        self.image = (pygame.image.load(characterInfo[5]))
        self.setSize(50, 75)
        self.position = (500, 400)
        self.valid = False
        
    def attack(self, target):
        hit = random.randint(1,100)
        if (hit >= target.dodge):
            damage = random.randint(1, self.atk)
            target.HP -= damage
            self.valid = True
    
    def SPattack(self, target):
        if (self.MP >= 4):
            self.valid = True
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
                 enemyInfo):
        super().__init__(scene)
        
        self.HP = enemyInfo[1]
        self.atk = enemyInfo[2]
        self.dodge = enemyInfo[3]
        self.name = enemyInfo[0]
        self.spat = self.atk*3
        self.image = (pygame.image.load(enemyInfo[4]))
        self.setSize(50, 75)
        self.position = (120, 400)
        
    def attack(self, target):
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
    def __init__(self, selectedChar, randEnemy):
        super().__init__()
        self.setImage("white.jpg")
        
        self.outcome = 0
        
        Characters = {
            0: ["Sonic", 6, 7, 80, 16, "sonicWPlaceholder.png"],
            1: ["Surge", 10, 10, 30, 8, "Surge_Placeholder.png"],
            2: ["Agent Three", 3, 8, 75, 12, "Agent_3_Placeholder.png"]
            }
        
        enemyTable = {
            0: ["Skelly", 10, 1, 40, "skeleton_captain.png"],
            1: ["Fire Slime", 5, 4, 25, "fireSlime.png"],
            2: ["Kompa", 1, 2, 90, "Boss.png"]
            }
        
        self.activeCharacter = Character(self, Characters[selectedChar])
        self.Enemies = Enemies(self, enemyTable[randEnemy])
        
        self.lblcharhealth = simpleGE.MultiLabel()
        self.lblcharhealth.textLines = [
            f"{self.activeCharacter.name},",
            f"HP: {self.activeCharacter.HP}",
            f"MP: {self.activeCharacter.MP}"
                                         ]
        self.lblcharhealth.center = (500, 100)
        
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
        
        self.sprites = [self.activeCharacter,
                        self.Enemies,
                        self.lblcharhealth,
                        self.lblenemyhealth,
                        self.lblfeed,
                        self.lblenemyactions]
        
    def processEvent(self, event):
        if event.type == pygame.KEYDOWN:
            self.activeCharacter.valid = False
            if event.key ==  pygame.K_a:
                self.lblfeed.text = (f"{self.activeCharacter.name} attacks {self.Enemies.name}")
                self.activeCharacter.attack(self.Enemies)
                self.lblenemyhealth.text = (f"{self.Enemies.name} HP: {self.Enemies.HP}")
                if self.activeCharacter.valid == True:
                    self.enemyAttacks()
            if event.key ==  pygame.K_s:
                self.activeCharacter.SPattack(self.Enemies)
                if self.activeCharacter.enough == 1:
                    self.lblcharhealth.textLines = [
                        f"{self.activeCharacter.name},",
                        f"HP: {self.activeCharacter.HP}",
                        f"MP: {self.activeCharacter.MP}"
                                                     ]
                    self.lblfeed.text = (f"{self.activeCharacter.name} uses spcial attack on {self.Enemies.name}")
                if self.activeCharacter.enough == 0:
                    self.lblfeed.text = ("You dont have enough MP")
                self.lblenemyhealth.text = (f"{self.Enemies.name} HP: {self.Enemies.HP}")
                if self.activeCharacter.valid == True:
                    self.enemyAttacks()
            
    def enemyAttacks(self):
        self.lblenemyactions.text = (f"{self.Enemies.name} attacks {self.activeCharacter.name}")
        self.Enemies.attack(self.activeCharacter)
        self.lblcharhealth.textLines = [
            f"{self.activeCharacter.name},",
            f"HP: {self.activeCharacter.HP}",
            f"MP: {self.activeCharacter.MP}"
                                         ]
                
    def process(self):
        if self.activeCharacter.HP <= 0:
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
        
        self.Enemy = 0
        
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
        
        self.charSelect = 0
        
        self.outcome = outcome
        
        self.sprites = [self.instructions,
                        self.btnPlay,
                        self.btnQuit,
                        self.charSelectSprite]
                
    def process(self):
        self.Enemy = random.randint(0,2)
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
                if self.charSelect >= 3:
                    self.charSelect = 0
            if self.isKeyPressed(pygame.K_LEFT):
                self.charSelect -= 1
                if self.charSelect <= -1:
                    self.charSelect = 2
            if self.charSelect == 0:
                self.charSelectSprite.image = pygame.image.load("sonicWPlaceholder.png")
                self.charSelectSprite.setSize(50, 75)
                self.charSelectSprite.position = (320, 50)
            if self.charSelect == 1:
                self.charSelectSprite.image = pygame.image.load("Surge_Placeholder.png")
                self.charSelectSprite.setSize(50, 75)
                self.charSelectSprite.position = (320, 50)
            if self.charSelect == 2:
                self.charSelectSprite.image = pygame.image.load("Agent_3_Placeholder.png")
                self.charSelectSprite.setSize(50, 75)
                self.charSelectSprite.position = (320, 50)

def main():
    keepGoing = True
    outcome = 0
    while keepGoing:
        instructions = TitleScreen(outcome)
        instructions.start()
        selectedChar = instructions.charSelect
        randEnemy = instructions.Enemy
        if instructions.response == "Play":
            battle = BattleScene(selectedChar, randEnemy)
            battle.start()
            outcome = battle.outcome
        else:
            keepGoing = False
        
if __name__ == "__main__":
    main()