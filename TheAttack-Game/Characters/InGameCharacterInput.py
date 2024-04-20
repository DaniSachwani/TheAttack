import pygame
from Characters import InGameCharacter
from Common import Common
class InGameCharacterInput(InGameCharacter.InGameCharacter):

    def __init__(self,character,location,arena):
        super().__init__(character,arena)
        self.Character.location = location

    def HandleMovementUsingButtons(self, WIN, FONT, WIDTH, HEIGHT,Key):

        if(Key == Common.Bconfig.buttonConfigs[0].Up):
            self.Character.KeyPress="Up"
        elif(Key == Common.Bconfig.buttonConfigs[0].Down):
            self.Character.KeyPress="Down"
        if(Key == Common.Bconfig.buttonConfigs[0].Left):
            self.Character.KeyPress="Left"
        elif(Key == Common.Bconfig.buttonConfigs[0].Right):
            self.Character.KeyPress="Right"

        if(Key == Common.Bconfig.buttonConfigs[0].Action1):
            self.Character.KeyPress="Action1"

        if(Key == None):
            self.Character.KeyPress=""

        return self.Character.location