from Renderer import Renderer
import pygame
class Arena(Renderer):

    PartsImages =[]
    playerlocation =[0,0]
    location =[0,0]
    def __init__(self,obj):
        self.Name = ""
        self.Parts = []
        if obj != None:
            self.Name = obj.Name
            self.Parts = obj.Parts

        for part in self.Parts:
            self.PartsImages.append( pygame.image.load(part.BackgroundImage))
    
    def Render(self, WIN, FONT, WIDTH, HEIGHT):
        backimage = None
        i=0
        camera_location = [0,0] 
        for partimage in self.PartsImages:
            arenasize = {
                "X":self.Parts[0].WalkingArea.X,
                "Y":self.Parts[0].WalkingArea.Y,
                "Width":self.PartsImages[0].get_width(),
                "Height":self.PartsImages[0].get_height()
            }
            backimage = pygame.Surface((WIDTH, HEIGHT))
            if(self.playerlocation[0]> arenasize["X"]+ WIDTH/2):
                camera_location[0]= -(self.playerlocation[0]-WIDTH/2)
            if(self.playerlocation[0]> arenasize["Width"]- WIDTH/2):
                camera_location[0]= -(arenasize["Width"]- WIDTH)
            if(self.playerlocation[1]> arenasize["Y"]+ HEIGHT/2):
                camera_location[1]= -(self.playerlocation[1]-HEIGHT/2-300)
            if(self.playerlocation[1]> arenasize["Height"]- HEIGHT/2):
                camera_location[1]= -(arenasize["Height"]- HEIGHT-300) 

            backimage.blit(partimage, (camera_location[0], camera_location[1]))
            self.location=[camera_location[0], camera_location[1]]
            i+=1    

        return backimage

    def RenderWithNavigate(self, WIN, FONT, WIDTH, HEIGHT, Key):
        pass

    def InWalkingArea(self,location):
        allowed = False
        for part in self.Parts:
            if(location[0] > part.WalkingArea.X 
               and location[0] < part.WalkingArea.X + part.WalkingArea.Width
               and location[1] > part.WalkingArea.Y
               and location[1] < part.WalkingArea.Y + part.WalkingArea.Height
               ):
                allowed =True

        return allowed
    
    def GetSize(self):
        Size = {
            "X":self.Parts[0].WalkingArea.X,
            "Y":self.Parts[0].WalkingArea.Y,
            "Width":self.PartsImages[0].get_width(),
            "Height":self.PartsImages[0].get_height()
        }
        return Size
    