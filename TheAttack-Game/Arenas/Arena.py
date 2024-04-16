from Renderer import Renderer
import pygame
class Arena(Renderer):

    PartsImages =[]
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
        for partimage in self.PartsImages:
            backimage = pygame.Surface((partimage.get_width(), partimage.get_height()))
            backimage.blit(partimage, (self.Parts[i].DrawCoordinateX, self.Parts[i].DrawCoordinateY))
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
    