import os
from Common import Common
import json
from types import SimpleNamespace
from Arenas import Arena

class ArenaManager:

    arenasDir = Common.WorkingDir+"TheAttack-Game/Arenas/ArenaData/"
    Sconfig = None
    Bconfig = None

    def __init__(self):
        self.Arenas = []
        dir_list = os.listdir(self.arenasDir)
        # prints all files
        if(len(dir_list) > 0):
            self.ReadArenas(dir_list)

    def ReadArenas(self,dirlist):
        self.Arenas = []
        for file in dirlist:
            f = open(self.arenasDir+file, "r")
            arenaSerial = f.read()
            deserialized = json.loads(arenaSerial, object_hook=lambda d: SimpleNamespace(**d))
            self.Arenas.append(Arena.Arena(deserialized))
