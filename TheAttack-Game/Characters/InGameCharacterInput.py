import pygame
from Characters import InGameCharacter
from Common import Common
class InGameCharacterInput(InGameCharacter.InGameCharacter):

    def __init__(self,character,location,arena):
        super().__init__(character,arena)
        self.Character.location = location

    def HandleMovementUsingButtons(self, WIN, FONT, WIDTH, HEIGHT,Key):

        self.Character.CurrentAction = "Standing"
        prevx = self.Character.location[0]
        prevy = self.Character.location[1]
        if(Key == Common.Bconfig.buttonConfigs[0].Up):
            self.Character.location[1]-= 25
            self.Character.CurrentAction = "Walking"
        elif(Key == Common.Bconfig.buttonConfigs[0].Down):
            self.Character.location[1]+= 25    
            self.Character.CurrentAction = "Walking"
        if(Key == Common.Bconfig.buttonConfigs[0].Left):
            self.Character.Facing = "Left" 
            self.Character.location[0]-= 25
            self.Character.CurrentAction = "Walking"
        elif(Key == Common.Bconfig.buttonConfigs[0].Right):
            self.Character.Facing = "Right"
            self.Character.location[0]+= 25
            self.Character.CurrentAction = "Walking"

        if(not self.Arena.InWalkingArea(self.Character.location)):
            self.Character.location[0] = prevx
            self.Character.location[1] = prevy
            
        #self.Character.Render( WIN, FONT, WIDTH, HEIGHT)

        return self.Character.location