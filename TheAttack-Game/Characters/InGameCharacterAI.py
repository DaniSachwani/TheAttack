import pygame
from Characters import InGameCharacter
class InGameCharacterAI(InGameCharacter.InGameCharacter):

    def __init__(self,character,location,arena):
        super().__init__(character,arena)
        self.Character.location = location

    def HandleMovement(self, WIN, FONT, WIDTH, HEIGHT):
        self.Character.Render( WIN, FONT, WIDTH, HEIGHT)
        
