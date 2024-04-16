from Renderer import Renderer
import pygame
class Character(Renderer):

    currentFrame = 0
    ActionsImages ={}
    CurrentAction = "Standing"
    location = [0,0]
    Facing = "Right"
    last_time = None
    def __init__(self,obj):
        self.Name = ""
        self.Actions = []
        if obj != None:
            self.Name = obj["Name"]
            self.Actions = obj["Actions"]

        for ActionName,Frames in self.Actions.items():
            self.ActionsImages[ActionName] = []
            for frame in Frames:
                self.ActionsImages[ActionName].append( pygame.image.load(frame["Image"]))
        
        self.last_time = pygame.time.get_ticks()
    
    def Render(self, WIN, FONT, WIDTH, HEIGHT):
        if self.currentFrame >= len(self.Actions[self.CurrentAction]):
            self.currentFrame = 0     
        
        sprite = self.ActionsImages[self.CurrentAction][self.currentFrame]
        if(self.Facing == "Left"):
            sprite = pygame.transform.flip(sprite, True, False)
        WIN.blit(sprite, (self.location[0]-sprite.get_width()/2,self.location[1]-sprite.get_height()))

        #current_time = pygame.time.get_ticks()
        #if current_time - self.last_time >= self.Actions[self.CurrentAction][self.currentFrame]["DelaybeforeNextFrame"]:
        self.currentFrame+=1
        #    self.last_time = pygame.time.get_ticks()
    


    def RenderWithNavigate(self, WIN, FONT, WIDTH, HEIGHT, Key):
        pass