from Renderer import Renderer
from Common import Common
import pygame
from Characters import InGameCharacterInput
from Characters import InGameCharacterAI
import copy
class NewGame(Renderer):

    Characters = None
    Objects = None

    def __init__(self):
        self.Characters = [
            InGameCharacterInput.InGameCharacterInput(copy.deepcopy(Common.CharacterManager.Characters["Soldier"]),[400,400], Common.ArenaManager.Arenas[0]),
            InGameCharacterAI.InGameCharacterAI(copy.deepcopy(Common.CharacterManager.Characters["Soldier"]),[100,400], Common.ArenaManager.Arenas[0])
        ]
        self.Objects =[]

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
        
        i=0
        for char in self.Characters:
            if isinstance(char, InGameCharacterAI.InGameCharacterAI):
                char.Character.Render( backimage, FONT, WIDTH, HEIGHT)
                object = char.Character.GetSpawnObject()
                if(object != None):
                    self.Objects.append(object)
            else:
                char.Character.CameraShouldFollowPlayer=True
                char.Character.Render( backimage, FONT, WIDTH, HEIGHT)
                object = char.Character.GetSpawnObject()
                if(object != None):
                    self.Objects.append(object)
        j=0
        for obj in self.Objects:
            obj.Render( backimage, FONT, WIDTH, HEIGHT)
            if(obj.Destroyed ==True):
                del self.Objects[j]
            j+=1

        WIN.blit(backimage, (camera_location[0],camera_location[1]))
        pygame.display.update()    

