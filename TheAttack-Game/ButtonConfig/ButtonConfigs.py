import os
from Common import Common
import json
from ButtonConfig import ButtonConfig
from types import SimpleNamespace
class ButtonConfigs:

    buttonConfigs = None
    configsDir = Common.WorkingDir+"TheAttack-Game/ButtonConfig/ButtonConfigFiles/"

    def __init__(self):
        dir_list = os.listdir(self.configsDir)
        # prints all files
        if(len(dir_list) > 0):
            self.DeSerializeConfigs(dir_list)
        else:
            self.SerializeFirstTimeConfigs()

    
    def SerializeFirstTimeConfigs(self):
        ButtonConfigs1 = ButtonConfig.ButtonConfig(True)
        ButtonConfigs2 = ButtonConfig.ButtonConfig(False)
        self.buttonConfigs = [ButtonConfigs1, ButtonConfigs2]
        i = 1
        for BConf in self.buttonConfigs:
            with open(self.configsDir+f'PlayerConfig{i}.json', 'w') as f:
                f.write(BConf.toJSON())
            i += 1

    def SerializeConfigs(self):
        i = 1
        for BConf in self.buttonConfigs:
            with open(self.configsDir+f'PlayerConfig{i}.json', 'w') as f:
                f.write(BConf.toJSON())
            i += 1

    def DeSerializeConfigs(self,dirlist):
        self.buttonConfigs = []
        for file in dirlist:
            f = open(self.configsDir+file, "r")
            buttonconfigSerial = f.read()
            deserialized = json.loads(buttonconfigSerial, object_hook=lambda d: SimpleNamespace(**d))
            self.buttonConfigs.append(ButtonConfig.ButtonConfig(True,deserialized))
