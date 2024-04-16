import pygame
import datetime
import Constants
from MainMenu.Options import NewGame
from MainMenu.Options import GameOption
from MainMenu.Options import Quit
from Renderer import Renderer
from Common import Common
#from ButtonConfig import ButtonConfigs

class MainMenu(Renderer):

    Options= None
    MenuOptions = []
    GuidingText = ""
    GameTitle = ""
    SelectedIndex = 0
    MenuInputDelay =0.2
    
    def __init__(self):
        
        self.MenuOptions = [
                ("New Game",160), 
                ("Options",140), 
                ("Quit",100)
            ]
        self.GuidingText = (f"Use '{pygame.key.name(Common.Bconfig.buttonConfigs[0].Up)}', '{pygame.key.name(Common.Bconfig.buttonConfigs[0].Down)}', '{pygame.key.name(Common.Bconfig.buttonConfigs[0].Left)}', '{pygame.key.name(Common.Bconfig.buttonConfigs[0].Right)}' to navigate. Press '{pygame.key.name(Common.Bconfig.buttonConfigs[0].Action1)}' to Select.",0)
        self.GameTitle = ("THE ATTACK",300)
        Common.Sconfig.SoundDictionary[Constants.Constant.MainMenuBackgroundSound].play()
        self.Options =[NewGame.NewGame(),GameOption.GameOption(self),Quit.Quit()]
        
    def Render(self, WIN, FONT, WIDTH, HEIGHT):

        self.displayText(self.GameTitle[0],self.GameTitle[1],50,WIDTH/2,HEIGHT/2-150,FONT,WIN)

        i=0
        x = WIDTH/2
        y = HEIGHT/2-50
        for opt,len in self.MenuOptions:
            if(i==self.SelectedIndex):
                self.displayText(opt,len*1.2,40,x,y,FONT,WIN)
            else:
                self.displayText(opt,len,30,x,y,FONT,WIN)
            i+= 1
            y+= 50        

        self.displayText(self.GuidingText[0],self.GuidingText[1],25,10,HEIGHT-40,FONT,WIN)        
        pygame.display.update()

    def RenderWithNavigate(self, WIN, FONT, WIDTH, HEIGHT, Key):
        
        if(Key==Common.Bconfig.buttonConfigs[0].Up and self.SelectedIndex >0):
            self.SelectedIndex -=1
            Common.Sconfig.SoundDictionary[Constants.Constant.MenuItemSound].play()

        elif(Key==Common.Bconfig.buttonConfigs[0].Down and self.SelectedIndex <2):
            self.SelectedIndex +=1
            Common.Sconfig.SoundDictionary[Constants.Constant.MenuItemSound].play()

        if(Key==Common.Bconfig.buttonConfigs[0].Action1):
            return self.SelectOption(self.SelectedIndex)
        
        self.Render(WIN, FONT, WIDTH, HEIGHT)
        return None;

    def SelectOption(self,index):
        Common.Sconfig.SoundDictionary[Constants.Constant.MenuSelectSound].play()
        return self.Options[index]


