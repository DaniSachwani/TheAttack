from Renderer import Renderer
import copy
import pygame
import datetime
import Constants
from MainMenu import MainMenu
from Common import Common
class GameOption(Renderer):

    MenuOptions = []
    Save = ("Save",100)
    Cancel = ("Cancel",140)
    Title =("Button Config",350)
    GuidingText = ""
    _started_at = datetime.datetime.now(datetime.UTC)  
    MenuInputDelay =0.2  
    SelectedIndex=0
    Parent = None
    Changing =False
    time_passed =0
    NewButtonConfig =None
    def __init__(self,parent):
        self.MenuOptions = [
                ("Player 1 Controls:",280),
                ("Up:",160), 
                ("Down:",160), 
                ("Left:",160),
                ("Right:",160), 
                ("Action1:",160), 
                ("Action2:",160), 
                ("Action3:",160), 
                ("Player 2 Controls:",280),
                ("Up:",160), 
                ("Down:",160), 
                ("Left:",160), 
                ("Right:",160), 
                ("Action1:",160), 
                ("Action2:",160), 
                ("Action3:",160),  
            ]
        self.GuidingText = (f"Use '{pygame.key.name(Common.Bconfig.buttonConfigs[0].Up)}', '{pygame.key.name(Common.Bconfig.buttonConfigs[0].Down)}', '{pygame.key.name(Common.Bconfig.buttonConfigs[0].Left)}', '{pygame.key.name(Common.Bconfig.buttonConfigs[0].Right)}' to navigate. Press '{pygame.key.name(Common.Bconfig.buttonConfigs[0].Action1)}' to Select.",0)
        self.Parent= parent
        self.NewButtonConfig = copy.deepcopy(Common.Bconfig)
        
    def GetButtonText(self,index,player2):
        pIndex = 0
        if(player2):
            pIndex = 1
            index= index-8
        if(index ==1):
            return pygame.key.name(self.NewButtonConfig.buttonConfigs[pIndex].Up)                  
        if(index ==2):
            return pygame.key.name(self.NewButtonConfig.buttonConfigs[pIndex].Down)
        if(index ==3):
            return pygame.key.name(self.NewButtonConfig.buttonConfigs[pIndex].Left)
        if(index ==4):
            return pygame.key.name(self.NewButtonConfig.buttonConfigs[pIndex].Right)
        if(index ==5):
            return pygame.key.name(self.NewButtonConfig.buttonConfigs[pIndex].Action1)
        if(index ==6):
            return pygame.key.name(self.NewButtonConfig.buttonConfigs[pIndex].Action2)
        if(index ==7):
            return pygame.key.name(self.NewButtonConfig.buttonConfigs[pIndex].Action3)

        return ""

    def Render(self, WIN, FONT, WIDTH, HEIGHT):
        self.time_passed = datetime.datetime.now(datetime.UTC) - self._started_at
        self.displayText(self.Title[0],self.Title[1],50,WIDTH/2,HEIGHT/2-350,FONT,WIN)

        i=0
        j=0
        x = WIDTH/2 -250
        y = HEIGHT/2-200
        for opt,len in self.MenuOptions:
            if(i==0 or i==8):
                self.displayText(opt,len,30,x,y,FONT,WIN)
                self.displayText(self.GetButtonText(i,i>7),len,30,x+150,y,FONT,WIN)
                if(j==7):
                    j+=1
            else:
                if(j==self.SelectedIndex):
                    self.displayText(opt,len*1.2,40,x,y,FONT,WIN)
                    if(self.Changing == True):
                        if(self.time_passed.total_seconds() > 1):
                            self._started_at = datetime.datetime.now(datetime.UTC)
                            self.displayText(self.GetButtonText(i,i>7),len*1.2,40,x+200,y,FONT,WIN) 
                    else:
                        self.displayText(self.GetButtonText(i,i>7),len*1.2,40,x+200,y,FONT,WIN)
                    
                else:
                    self.displayText(opt,len,30,x,y,FONT,WIN)
                    self.displayText(self.GetButtonText(i,i>7),len,30,x+150,y,FONT,WIN)
                j+= 1
            
            i+= 1
            y+= 50
            if (i%8 == 0):
                y= HEIGHT/2-200
                x = WIDTH/2 +250        

        self.displayText(self.GuidingText[0],self.GuidingText[1],25,10,HEIGHT-40,FONT,WIN)        
        if(self.SelectedIndex ==15):
            self.displayText(self.Save[0],self.Save[1]*1.2,35,WIDTH-30,HEIGHT-40,FONT,WIN)
        else:
            self.displayText(self.Save[0],self.Save[1],25,WIDTH-30,HEIGHT-40,FONT,WIN)        
        
        if(self.SelectedIndex ==7):
            self.displayText(self.Cancel[0],self.Cancel[1],35,WIDTH-155,HEIGHT-40,FONT,WIN)        
        else:
            self.displayText(self.Cancel[0],self.Cancel[1]*1.2,25,WIDTH-130,HEIGHT-40,FONT,WIN)        
        
        pygame.display.update()


    def RenderWithNavigate(self, WIN, FONT, WIDTH, HEIGHT, Key):
        if(self.Changing == False):
            if(Key ==Common.Bconfig.buttonConfigs[0].Up and self.SelectedIndex >0):
                self.SelectedIndex -=1
                Common.Sconfig.SoundDictionary[Constants.Constant.MenuItemSound].play()

            elif(Key==Common.Bconfig.buttonConfigs[0].Down and self.SelectedIndex <15):
                self.SelectedIndex +=1
                Common.Sconfig.SoundDictionary[Constants.Constant.MenuItemSound].play()
            
            elif(Key==Common.Bconfig.buttonConfigs[0].Left and self.SelectedIndex-8 >=0):
                self.SelectedIndex -=8
                Common.Sconfig.SoundDictionary[Constants.Constant.MenuItemSound].play()

            elif(Key==Common.Bconfig.buttonConfigs[0].Right and self.SelectedIndex+8 <=15):
                self.SelectedIndex +=8
                Common.Sconfig.SoundDictionary[Constants.Constant.MenuItemSound].play()
    
            if(Key==Common.Bconfig.buttonConfigs[0].Action1):
                return self.SelectOption(self.SelectedIndex)        

        else:
            if(Key != None):
                self.ChangeKey(self.SelectedIndex,self.SelectedIndex>7,Key)
        
        self.Render(WIN, FONT, WIDTH, HEIGHT)
    
        return None
    
    def SelectOption(self,index):
        Common.Sconfig.SoundDictionary[Constants.Constant.MenuSelectSound].play()

        if(index ==15):
            Common.Bconfig =self.NewButtonConfig
            Common.Bconfig.SerializeConfigs()
            return self.Parent
        
        elif(index ==7):
            return self.Parent
        else:
            self.Changing =True

        return None

    def ChangeKey(self,index,player2,Key):
        pIndex = 0
        if(player2):
            pIndex = 1
            index= index-8
        if(index ==0):
            self.NewButtonConfig.buttonConfigs[pIndex].Up = Key                 
        if(index ==1):
            self.NewButtonConfig.buttonConfigs[pIndex].Down = Key
        if(index ==2):
            self.NewButtonConfig.buttonConfigs[pIndex].Left = Key
        if(index ==3):
            self.NewButtonConfig.buttonConfigs[pIndex].Right = Key
        if(index ==4):
            self.NewButtonConfig.buttonConfigs[pIndex].Action1 = Key
        if(index ==5):
            self.NewButtonConfig.buttonConfigs[pIndex].Action2 = Key
        if(index ==6):
            self.NewButtonConfig.buttonConfigs[pIndex].Action3 = Key
        self.Changing=False
    