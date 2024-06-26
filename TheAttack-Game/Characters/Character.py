from Renderer import Renderer
import pygame
import Common
import copy
class Character(Renderer):

    currentFrame = 0
    ActionsImages ={}
    SoundAudios ={}
    CurrentAction = "Standing"
    KeyPress = ""
    location = [0,0]
    Facing = "Right"
    last_time = None
    arenasize ={}
    CameraShouldFollowPlayer =False
    prevaction = None
    Arena =None
    ActionToReplace = None
    ObjectsToSpawn=[]
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
        
        prevx = self.location[0]
        prevy = self.location[1]

        if(self.KeyPress == "Up"and self.CurrentAction == "Walking"):
            self.location[1]-= 25
        elif(self.KeyPress == "Down"and self.CurrentAction == "Walking"):
            self.location[1]+= 25    
        if(self.KeyPress == "Left"and self.CurrentAction == "Walking"):
            self.Facing = "Left" 
            self.location[0]-= 25
        elif(self.KeyPress == "Right"and self.CurrentAction == "Walking"):
            self.Facing = "Right"
            self.location[0]+= 25
        
        if(not self.Arena.InWalkingArea(self.location,False)):
            self.location[0] = prevx
            self.location[1] = prevy
        
        ActionReplaced = False
        self.prevaction = self.CurrentAction
        if("OnAction" in self.Actions[self.CurrentAction][self.currentFrame]):
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

        sprite = self.ActionsImages[self.CurrentAction][self.currentFrame]
        if(self.Facing == "Left"):
            sprite = pygame.transform.flip(sprite, True, False)

        if(ActionReplaced or current_time - self.last_time >= self.Actions[self.CurrentAction][self.currentFrame]["DelaybeforeNextFrame"]):
            if("SoundName" in self.Actions[self.CurrentAction][self.currentFrame]):
                self.SoundAudios[self.Actions[self.CurrentAction][self.currentFrame]["SoundName"]].play()

            self.currentFrame+=1

            if self.currentFrame >= len(self.Actions[self.CurrentAction] or ActionReplaced):
                self.currentFrame = 0     

            self.last_time = pygame.time.get_ticks()

            if("SpawnObject" in self.Actions[self.CurrentAction][self.currentFrame]):
                objectSpawnData = self.Actions[self.CurrentAction][self.currentFrame]["SpawnObject"]

                for data in objectSpawnData:
                    objectcopy = copy.deepcopy(Common.Common.ObjectsManager.Objects[data["Name"]])
                    if (self.Facing=="Left"):                
                        objectcopy.location = [self.location[0]-sprite.get_width()/2+data["X"],self.location[1]-sprite.get_height()+data["Y"]]#[0]- sprite.get_width()
                    else:
                        objectcopy.location = [self.location[0]+sprite.get_width()/2-data["X"],self.location[1]-sprite.get_height()+data["Y"]]#[0]- sprite.get_width()
                    objectcopy.Arena = self.Arena
                    objectcopy.Facing = self.Facing
                    self.ObjectsToSpawn.append(objectcopy)
        
        if(self.CameraShouldFollowPlayer):
            camera_location=[self.location[0],self.location[1]]
            if(self.location[0]> self.arenasize["X"]+ WIDTH/2):
                camera_location[0]= WIDTH/2
            if(self.location[0]> self.arenasize["Width"]- WIDTH/2):
                camera_location[0]= self.location[0]-(self.arenasize["Width"]- WIDTH)
            if(self.location[1]> self.arenasize["Y"]+ HEIGHT/2):
                camera_location[1]= HEIGHT/2 +300
            if(self.location[1]> self.arenasize["Height"]- HEIGHT/2):
                camera_location[1]= self.location[1]-(self.arenasize["Height"]- HEIGHT-300 )

            Displacement = {"X":0,"Y":0}

            if("Displacement" in self.Actions[self.CurrentAction][self.currentFrame]):
                Displacement = self.Actions[self.CurrentAction][self.currentFrame]["Displacement"]
            
            WIN.blit(sprite, (camera_location[0]-sprite.get_width()/2+Displacement["X"],camera_location[1]-sprite.get_height()++Displacement["Y"]))

        else:
            camera_location=[self.location[0]+self.Arena.location[0],self.location[1]+self.Arena.location[1]]

            Displacement = {"X":0,"Y":0}

            if("Displacement" in self.Actions[self.CurrentAction][self.currentFrame]):
                Displacement = self.Actions[self.CurrentAction][self.currentFrame]["Displacement"]

            WIN.blit(sprite, (camera_location[0]-sprite.get_width()/2+Displacement["X"],camera_location[1]-sprite.get_height()+Displacement["Y"]))

        


    def RenderWithNavigate(self, WIN, FONT, WIDTH, HEIGHT, Key):
        pass

    def GetSpawnObject(self):
        if len(self.ObjectsToSpawn) == 0:
            return None
        else:
            obj = self.ObjectsToSpawn[0]
            del self.ObjectsToSpawn[0]
            return obj