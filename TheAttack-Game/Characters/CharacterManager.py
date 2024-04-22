import os
from Common import Common
import json
from types import SimpleNamespace
from Characters import Character

class CharacterManager:

    charactersDir = Common.WorkingDir+"TheAttack-Game/Characters/CharactersData/"
    Sconfig = None
    Bconfig = None

    def __init__(self):
        self.Characters = {}
        dir_list = os.listdir(self.charactersDir)
        # prints all files
        if(len(dir_list) > 0):
            self.ReadCharacters(dir_list)

    def ReadCharacters(self,dirlist):
        self.Characters = {}
        for file in dirlist:
            f = open(self.charactersDir+file, "r")
            CharacterSerial = f.read()
            deserialized = json.loads(CharacterSerial)
            self.Characters[file.split(".")[0]] = Character.Character(deserialized)
