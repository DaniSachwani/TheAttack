from Renderer import Renderer
import pygame
import Common

class Quit(Renderer):

    def Render(self, WIN, FONT, WIDTH, HEIGHT):
        Common.Common.Run = False

    def RenderWithNavigate(self, WIN, FONT, WIDTH, HEIGHT, Key):
        self.Render( WIN, FONT, WIDTH, HEIGHT)
    