from Renderer import Renderer
from Common import Common
import pygame
from Characters import InGameCharacterInput
from Characters import InGameCharacterAI
import copy
class NewGame(Renderer):

    Characters = None

    def __init__(self):
        self.Characters = [
            InGameCharacterInput.InGameCharacterInput(copy.deepcopy(Common.CharacterManager.Characters[0]),[400,400], Common.ArenaManager.Arenas[0]),
            InGameCharacterAI.InGameCharacterAI(copy.deepcopy(Common.CharacterManager.Characters[0]),[100,400], Common.ArenaManager.Arenas[0])
        ]
    
    def Render(self, WIN, FONT, WIDTH, HEIGHT):
        pass 
        
        
    def RenderWithNavigate(self, WIN, FONT, WIDTH, HEIGHT, Key):

        for i in range(len(self.Characters)):
            for j in range(len(self.Characters)):
               if(i!=j and self.Characters[i].Character.location[1]<self.Characters[j].Character.location[1] ):
                   self.Characters[i],self.Characters[j]=self.Characters[j],self.Characters[i]

        playerlocations = []
        humanplayerindex =0
        i=0
        for char in self.Characters:
            if isinstance(char, InGameCharacterAI.InGameCharacterAI):
                playerlocations.append(char.HandleMovement(WIN, FONT, WIDTH, HEIGHT))
            else:
                humanplayerindex = i
                playerlocations.append(char.HandleMovementUsingButtons(WIN, FONT, WIDTH, HEIGHT, Key))
            i+=1
        #backimage = self.Render(WIN, FONT, WIDTH, HEIGHT)
        
        camera_location = [0,0] 
        Common.ArenaManager.Arenas[0].playerlocation= playerlocations[humanplayerindex]
        backimage = Common.ArenaManager.Arenas[0].Render(WIN, FONT, WIDTH, HEIGHT)
        
        arenasize = Common.ArenaManager.Arenas[0].GetSize()
        i=0
        for char in self.Characters:
            if isinstance(char, InGameCharacterAI.InGameCharacterAI):
                char.Character.arenasize = arenasize
                char.Character.arenalocation = Common.ArenaManager.Arenas[0].location
                char.Character.Render( backimage, FONT, WIDTH, HEIGHT)
            else:
                char.Character.arenasize = arenasize
                char.Character.arenalocation = Common.ArenaManager.Arenas[0].location
                char.Character.CameraShouldFollowPlayer=True
                char.Character.Render( backimage, FONT, WIDTH, HEIGHT)


        WIN.blit(backimage, (camera_location[0],camera_location[1]))
        pygame.display.update()    

