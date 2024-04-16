import pygame

class Renderer:

    def Render(self, WIN, FONT, WIDTH, HEIGHT):
        pass

    def displayText(self,Text,TextLen,FontSize,PosX,PosY,FONT,WIN):
        FONT = pygame.font.SysFont("consolas",FontSize)
        text = FONT.render(Text,1,"white")
        WIN.blit(text, (PosX-TextLen/2,PosY))
    

    def RenderWithNavigate(self, WIN, FONT, WIDTH, HEIGHT, Key):
        pass