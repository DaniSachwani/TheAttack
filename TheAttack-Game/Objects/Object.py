from Renderer import Renderer
import pygame
import Common
class Object(Renderer):

    currentFrame = 0
    ActionsImages ={}
    SoundAudios ={}
    CurrentAction = "Standing"
    KeyPress = ""
    location = [0,0,0]
    Facing = "Right"
    last_time = None
    arenasize ={}
    CameraShouldFollowPlayer =False
    prevaction = None
    Arena =None
    ActionToReplace = None
    Destroyed = False
    ReachedAWall= False
    def __init__(self,obj):
        self.Name = ""
        self.Actions = []
        self.Sounds = {}
        if obj != None:
            self.Name = obj["Name"]
            self.Actions = obj["Actions"]
            self.Sounds= obj["Sounds"]

        for ActionName,Frames in self.Actions.items():
            self.ActionsImages[ActionName] = []
            for frame in Frames:
                self.ActionsImages[ActionName].append( pygame.image.load(frame["Image"]))
        
        for SoundName,SoundFile in self.Sounds.items():
            self.SoundAudios[SoundName]= pygame.mixer.Sound(Common.Common.SoundsDir+"/"+SoundFile)

        self.CurrentAction = next(iter(self.Actions))
        self.ActionToReplace = self.CurrentAction
        self.last_time = pygame.time.get_ticks()
    
    def Render(self, WIN, FONT, WIDTH, HEIGHT):
        
        ActionReplaced = False
        self.prevaction = self.CurrentAction
        if("OnAction" in self.Actions[self.CurrentAction][self.currentFrame]):
            if("Destroy" in self.Actions[self.CurrentAction][self.currentFrame]["OnAction"]):
                if(self.Actions[self.CurrentAction][self.currentFrame]["OnAction"]["Destroy"] ==""):
                    self.Destroyed = True
                elif(self.Actions[self.CurrentAction][self.currentFrame]["OnAction"]["Destroy"] =="Hit"):
                    if(self.ReachedAWall):
                        self.Destroyed = True
                
                #elif(self.Actions[self.CurrentAction][self.currentFrame]["OnAction"]["Destroy"] ==""):
                #todo when hit

            if(self.KeyPress !=""):
                if(self.KeyPress in self.Actions[self.CurrentAction][self.currentFrame]["OnAction"] ):
                    self.ActionToReplace = self.Actions[self.CurrentAction][self.currentFrame]["OnAction"][self.KeyPress]
                    if(self.CurrentAction != self.prevaction or self.Actions[self.CurrentAction][self.currentFrame]["DelaybeforeNextAction"]==True):
                        ActionReplaced = True
            else:
                self.ActionToReplace = next(iter(self.Actions))

        current_time = pygame.time.get_ticks()
        if ActionReplaced or self.Actions[self.CurrentAction][self.currentFrame]["DelaybeforeNextAction"]==False or (self.Actions[self.CurrentAction][self.currentFrame]["DelaybeforeNextAction"]==True and current_time - self.last_time >= self.Actions[self.CurrentAction][self.currentFrame]["DelaybeforeNextFrame"]):
            
            self.CurrentAction = self.ActionToReplace   
            if(self.CurrentAction != self.prevaction):
                self.currentFrame = 0


            if("Move" in self.Actions[self.CurrentAction][self.currentFrame]):
                prevx = self.location[0]
                prevy = self.location[1]
            
                if(self.Facing =="Right"):
                    self.location[0] += self.Actions[self.CurrentAction][self.currentFrame]["Move"]["DisplacmentX"]
                else:
                    self.location[0] -= self.Actions[self.CurrentAction][self.currentFrame]["Move"]["DisplacmentX"]

                self.location[1] += self.Actions[self.CurrentAction][self.currentFrame]["Move"]["DisplacmentY"]

                if(not self.Arena.InWalkingArea(self.location,True)):
                    self.ReachedAWall = True
                    self.location[0] = prevx
                    self.location[1] = prevy

        
        if(ActionReplaced or current_time - self.last_time >= self.Actions[self.CurrentAction][self.currentFrame]["DelaybeforeNextFrame"]):
            if("SoundName" in self.Actions[self.CurrentAction][self.currentFrame]):
                self.SoundAudios[self.Actions[self.CurrentAction][self.currentFrame]["SoundName"]].play()

            self.currentFrame+=1

            if self.currentFrame >= len(self.Actions[self.CurrentAction]):
                self.currentFrame = 0     

            self.last_time = pygame.time.get_ticks()

        sprite = self.ActionsImages[self.CurrentAction][self.currentFrame]
        if(self.Facing == "Left"):
            sprite = pygame.transform.flip(sprite, True, False)

    
        camera_location=[self.location[0]+self.Arena.location[0],self.location[1]-self.Arena.location[1]-self.location[2]]

        Displacement = {"X":0,"Y":0}

        if("Displacement" in self.Actions[self.CurrentAction][self.currentFrame]):
            Displacement = self.Actions[self.CurrentAction][self.currentFrame]["Displacement"]

        WIN.blit(sprite, (camera_location[0]-sprite.get_width()/2+Displacement["X"],camera_location[1]-sprite.get_height()+Displacement["Y"]))

        
    def RenderWithNavigate(self, WIN, FONT, WIDTH, HEIGHT, Key):
        pass

    def GetHitBoxes(self):
        resultarr = []
        if("HitBoxes" in self.Actions[self.CurrentAction][self.currentFrame]): 
            arr = self.Actions[self.CurrentAction][self.currentFrame]["HitBoxes"]
            i = 0
            for index, element in enumerate(arr):
                tempsprite = self.ActionsImages[self.CurrentAction][self.currentFrame]
                if isinstance(element, list):
                    resultarr.append([self.location[0]-tempsprite.get_width()+arr[index][0],self.location[1]-tempsprite.get_height()+arr[index][1],arr[index][3],arr[index][4]])
                else:
                    tempsprite = self.ActionsImages[self.CurrentAction][self.currentFrame]
            
                    resultarr.append([self.location[0]-tempsprite.get_width(),self.location[1]-tempsprite.get_height(),tempsprite.get_width(),tempsprite.get_height()])
        return resultarr
    

    def PerformCollision(self,CollidedObject):
        pass

