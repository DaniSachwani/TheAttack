from Renderer import Renderer
import pygame
import Common
class Character(Renderer):

    currentFrame = 0
    ActionsImages ={}
    SoundAudios ={}
    CurrentAction = "Standing"
    location = [0,0]
    Facing = "Right"
    last_time = None
    arenalocation =[0,0]
    arenasize ={}
    CameraShouldFollowPlayer =False
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

        self.last_time = pygame.time.get_ticks()
    
    def Render(self, WIN, FONT, WIDTH, HEIGHT):
        if self.currentFrame >= len(self.Actions[self.CurrentAction]):
            self.currentFrame = 0     
        

        sprite = self.ActionsImages[self.CurrentAction][self.currentFrame]
        if(self.Facing == "Left"):
            sprite = pygame.transform.flip(sprite, True, False)

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

            WIN.blit(sprite, (camera_location[0]-sprite.get_width()/2,camera_location[1]-sprite.get_height()))

        else:
            camera_location=[self.location[0]+self.arenalocation[0],self.location[1]+self.arenalocation[1]]

            WIN.blit(sprite, (camera_location[0]-sprite.get_width()/2,camera_location[1]-sprite.get_height()))

        current_time = pygame.time.get_ticks()
        if current_time - self.last_time >= self.Actions[self.CurrentAction][self.currentFrame]["DelaybeforeNextFrame"]:
            if("SoundName" in self.Actions[self.CurrentAction][self.currentFrame]):
                self.SoundAudios[self.Actions[self.CurrentAction][self.currentFrame]["SoundName"]].play()

            self.currentFrame+=1
            self.last_time = pygame.time.get_ticks()
    


    def RenderWithNavigate(self, WIN, FONT, WIDTH, HEIGHT, Key):
        pass