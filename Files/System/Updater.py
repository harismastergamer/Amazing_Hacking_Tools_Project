import tkinter as tk
import os
import requests

AssetsConfigUrl = "https://raw.githubusercontent.com/harismastergamer/Amazing_Hacking_Tools_Project/main/Files/Assets/AssetConfig.yaml"


with open(os.path.dirname(os.path.abspath(__file__) + "/ScriptFolderLoc.txt"), "r") as InstallLocFile:
    InstallLoc = InstallLocFile.read()
    InstallLocFile.close()

print("InstallLoc: ",InstallLoc)

if not os.path.exists(InstallLoc + "/System/AssetsConfig.yaml"):
    response = requests.get(AssetsConfigUrl)
    with open(InstallLoc + "/System/AssetsConfig.yaml", "w") as AssetsConfigFile:
        AssetsConfigFile.write(response.content)
