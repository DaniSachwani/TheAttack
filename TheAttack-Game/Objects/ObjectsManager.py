import os
from Common import Common
import json
from types import SimpleNamespace

from Objects import Object

class ObjectsManager:

    objectsDir = Common.WorkingDir+"TheAttack-Game/Objects/ObjectsData/"
    Sconfig = None
    Bconfig = None

    def __init__(self):
        self.Objects = {}
        dir_list = os.listdir(self.objectsDir)
        # prints all files
        if(len(dir_list) > 0):
            self.ReadObjects(dir_list)

    def ReadObjects(self,dirlist):
        self.Objects = {}
        for file in dirlist:
            f = open(self.objectsDir+file, "r")
            ObjectSerial = f.read()
            deserialized = json.loads(ObjectSerial)
            self.Objects[file.split(".")[0]] = Object.Object(deserialized)
