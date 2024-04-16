import pygame
class InGameCharacter:

    Character = None
    Arena = None
    def __init__(self,character,arena):
        self.Character = character
        self.Arena = arena

    def HandleMovement(self, WIN, FONT, WIDTH, HEIGHT):
        pass

    def HandleMovementUsingButtons(self, WIN, FONT, WIDTH, HEIGHT,Key):
        pass
