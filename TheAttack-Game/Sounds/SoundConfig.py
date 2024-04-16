import pygame
import json
import Common 
class SoundConfig:

    SoundPathDictionary = None
    SoundDictionary =None
    def __init__(self):
        self.Loadsound()

    def Loadsound(self):
        self.SoundPathDictionary = []
        f = open(Common.Common.SoundsConfigFilePath, "r")
        soundconfigSerial = f.read()
        deserialized = json.loads(soundconfigSerial)
        self.SoundPathDictionary =deserialized

        self.SoundDictionary ={}
        for key, value in self.SoundPathDictionary.items():
            self.SoundDictionary[key] = pygame.mixer.Sound(Common.Common.SoundsDir+"/"+value);