import tkinter as tk
import os
global InstallLoc


with open(os.path.dirname(os.path.abspath(__file__)), "r") as InstallLocFile:
    InstallLoc = InstallLocFile.read()
    InstallLocFile.close()

print(InstallLoc)

