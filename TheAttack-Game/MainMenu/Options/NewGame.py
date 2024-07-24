from Renderer import Renderer
from Common import Common
import pygame
from Characters import InGameCharacterInput
from Characters import InGameCharacterAI
from Objects.Object import Object
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
        AllObjects = []

        for char in self.Characters:
            AllObjects.append(char)
        for obj in self.Objects:
            AllObjects.append(obj)
        
        self.DetectCollision(AllObjects)
        for i in range(len(AllObjects)):
            for j in range(len(AllObjects)):
                if(i!=j):
                    Y1 = 0
                    Y2 = 0
                    if isinstance(AllObjects[i], Object):
                        Y1 = AllObjects[i].location[1]+ AllObjects[i].location[2]
                    else:
                        Y1 = AllObjects[i].Character.location[1]

                    if isinstance(AllObjects[j], Object):
                        Y2 = AllObjects[j].location[1]+ AllObjects[j].location[2]
                    else:
                        Y2 = AllObjects[j].Character.location[1]
                    
                    if(Y1 < Y2):            
                        AllObjects[i],AllObjects[j] =AllObjects[j],AllObjects[i]

        # for i in range(len(self.Characters)):
        #     for j in range(len(self.Characters)):
        #        if(i!=j and self.Characters[i].Character.location[1]<self.Characters[j].Character.location[1] ):
        #            self.Characters[i],self.Characters[j]=self.Characters[j],self.Characters[i]

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
        
        j=0
        for obj in AllObjects:
            if isinstance(obj, InGameCharacterAI.InGameCharacterAI):
                obj.Character.Render( backimage, FONT, WIDTH, HEIGHT)
                object = obj.Character.GetSpawnObject()
                if(object != None):
                    self.Objects.append(object)
            elif isinstance(obj, InGameCharacterInput.InGameCharacterInput):
                obj.Character.CameraShouldFollowPlayer=True
                obj.Character.Render( backimage, FONT, WIDTH, HEIGHT)
                object = obj.Character.GetSpawnObject()
                if(object != None):
                    self.Objects.append(object)
            else:
                obj.Render(backimage, FONT, WIDTH, HEIGHT)
            j+=1

        j=0
        for obj in self.Objects:
            if(obj.Destroyed ==True):
                del self.Objects[j]
            j+=1;
        
        WIN.blit(backimage, (camera_location[0],camera_location[1]))
        pygame.display.update()    

    def DetectCollision(self,AllObjects):
        for i in range(len(AllObjects)):
            for j in range(len(AllObjects)):
                if(i!=j):
                    BoxesArr1 =[]
                    if isinstance(AllObjects[i], Object):
                        BoxesArr1 = AllObjects[i].GetHitBoxes()
                    else:
                        BoxesArr1 = AllObjects[i].Character.GetHitBoxes()

                    if isinstance(AllObjects[j], Object):
                        BoxesArr2 = AllObjects[j].GetHitBoxes()
                    else:
                        BoxesArr2 = AllObjects[j].Character.GetHitBoxes()
                    
                    isHit = False
                    for Box1 in BoxesArr1:
                        for Box2 in BoxesArr2:
                            isHit = self.is_collision(Box1,Box2)
                        
                    if(isHit):
                        if isinstance(AllObjects[i], Object):
                            if isinstance(AllObjects[j], Object):
                                AllObjects[i].PerformCollision(AllObjects[j]);
                            else:
                                AllObjects[i].PerformCollision(AllObjects[j].Character);                            
                        else:
                            if isinstance(AllObjects[j], Object):
                                AllObjects[i].Character.PerformCollision(AllObjects[j]);
                            else:
                                AllObjects[i].Character.PerformCollision(AllObjects[j].Character);
                        
        pass

    def is_collision(self,box1, box2):
        x1, y1, w1, h1 = box1
        x2, y2, w2, h2 = box2

        horizontal_overlap = (x1 < x2 + w2) and (x2 < x1 + w1)
        
        vertical_overlap = (y1 < y2 + h2) and (y2 < y1 + h1)

        return horizontal_overlap and vertical_overlap
    

