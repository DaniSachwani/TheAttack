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
        return Common.ArenaManager.Arenas[0].Render(WIN, FONT, WIDTH, HEIGHT)
        
        
    def RenderWithNavigate(self, WIN, FONT, WIDTH, HEIGHT, Key):
        backimage = self.Render(WIN, FONT, WIDTH, HEIGHT)
        playerlocation = [0,0]
        for char in self.Characters:
            if isinstance(char, InGameCharacterAI.InGameCharacterAI):
                char.HandleMovement(backimage, FONT, WIDTH, HEIGHT)
            else:
                playerlocation = char.HandleMovementUsingButtons(backimage, FONT, WIDTH, HEIGHT, Key)

        camera_location = [0,0] 
        arenasize = Common.ArenaManager.Arenas[0].GetSize()
        if(playerlocation[0]> arenasize["X"]+ WIDTH/2):
            camera_location[0]= -(playerlocation[0]-WIDTH/2)
        if(playerlocation[0]> arenasize["Width"]- WIDTH/2):
            camera_location[0]= -(arenasize["Width"]- WIDTH)
        if(playerlocation[1]> arenasize["Y"]+ HEIGHT/2):
            camera_location[1]= -(playerlocation[1]-HEIGHT/2-300)
        if(playerlocation[1]> arenasize["Height"]- HEIGHT/2):
            camera_location[1]= -(arenasize["Height"]- HEIGHT-300) 

        WIN.blit(backimage, (camera_location[0],camera_location[1]))
        pygame.display.update()    

