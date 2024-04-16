import pygame
import time
import random
from MainMenu import MainMenu
from ButtonConfig import ButtonConfigs
from Sounds import SoundConfig
from Arenas import ArenaManager
from Characters import CharacterManager
import Common
from MainMenu.Options import NewGame

pygame.init()
WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

WIDTH, HEIGHT = WIN.get_size()
pygame.display.set_caption("The Attack")


Common.Common.Bconfig = ButtonConfigs.ButtonConfigs()

Common.Common.Sconfig = SoundConfig.SoundConfig();

Common.Common.ArenaManager =  ArenaManager.ArenaManager();
Common.Common.CharacterManager =  CharacterManager.CharacterManager();

pygame.font.init()
FONT = pygame.font.SysFont("consolas",30)

def main():
    detectpressed = False
    #clock = pygame.time.Clock()
    RenderObj = MainMenu.MainMenu()
    while Common.Common.Run:
    
        #clock.tick(100)

        if(not detectpressed or (detectpressed and (key != Common.Common.Bconfig.buttonConfigs[0].Up
                                   and key != Common.Common.Bconfig.buttonConfigs[0].Down
                                   and key != Common.Common.Bconfig.buttonConfigs[0].Left
                                   and key != Common.Common.Bconfig.buttonConfigs[0].Right
                                   and key != Common.Common.Bconfig.buttonConfigs[1].Up
                                   and key != Common.Common.Bconfig.buttonConfigs[1].Down
                                   and key != Common.Common.Bconfig.buttonConfigs[1].Left
                                   and key != Common.Common.Bconfig.buttonConfigs[1].Right
                                   ))):
            key = None


        WIN.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Common.Common.Run = False
                break
            if event.type == pygame.KEYDOWN:
                key =event.key

            if event.type == pygame.KEYUP and event.key == key:
                key = None
    
        Returnobj = RenderObj.RenderWithNavigate(WIN,FONT,WIDTH,HEIGHT,key)

        if(isinstance(Returnobj,NewGame.NewGame)):
            detectpressed = True

        if(Returnobj != None):
            RenderObj = Returnobj;

        #draw()
    pygame.quit()

if __name__ == "__main__":
    main()