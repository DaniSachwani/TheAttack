import pygame
import json
class ButtonConfig:

    Up = None
    Down = None
    Left = None
    Right = None
    Action1 = None
    Action2 = None
    Action3 = None

    def __init__(self,IsP1,SN = None):
        if(SN != None):
            self.Up = SN.Up
            self.Down = SN.Down
            self.Left = SN.Left
            self.Right = SN.Right
            self.Action1 = SN.Action1
            self.Action2 = SN.Action2
            self.Action3 = SN.Action3
        else:
            if(IsP1 == True):
                self.Up = pygame.K_UP
                self.Down = pygame.K_DOWN
                self.Left = pygame.K_LEFT
                self.Right = pygame.K_RIGHT
                self.Action1 = pygame.K_a
                self.Action2 = pygame.K_s
                self.Action3 = pygame.K_d
            else:
                self.Up = pygame.K_KP8
                self.Down = pygame.K_KP5
                self.Left = pygame.K_KP4
                self.Right = pygame.K_KP6
                self.Action1 = pygame.K_n
                self.Action2 = pygame.K_m
                self.Action3 = pygame.K_LESS
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)