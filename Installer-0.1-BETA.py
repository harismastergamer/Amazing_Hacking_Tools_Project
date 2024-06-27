import tkinter as tk
from tkinter import filedialog
import subprocess
global InstallLoc
#defs
InstallLoc = ""

def FirstPage():
    nextbutton.place(x=435, y=365)
    welcomelabel.place(x=30, y=25)
    welcomelabel2.place(x=30, y=160)



def SecondPage():
    
    nextbutton.config(command=ThirdPage)

    selectinstalllocationbutton.place(x=250, y=200)
    SecondPageLabel.place(x=30,y=50)
    installlocationtextbox.place(x=125, y=200)
    page2instructionslabel.place(x=125, y=150)
    okbutton.place(x=435, y=365)
    
    welcomelabel2.destroy()
    welcomelabel.destroy()
    nextbutton.destroy()
    

def ThirdPage():
    
    selectinstalllocationbutton.destroy()
    SecondPageLabel.destroy()
    selectinstalllocationbutton.destroy()
    installlocationtextbox.destroy()
    page2instructionslabel.destroy()
    okbutton.destroy()
    areyousurelabel.place(x=125, y=100)
    yesbutton.place(x=435, y=365)
    nobutton.place(x=50, y=365)


def InstallLocCannonBeBlackError():
    print("error")
    InstallLocCannonBeBlackErrorWin = tk.Tk()
    InstallLocCannonBeBlackErrorWin.title("Error ⚠")
    InstallLocCannonBeBlackErrorWin.geometry("300x200")
    closebutton = tk.Button(InstallLocCannonBeBlackErrorWin,text="Close", command=InstallLocCannonBeBlackErrorWin.destroy)
    errorlabel = tk.Label(InstallLocCannonBeBlackErrorWin,text="The install Location Cannot Be Empty!")
    closebutton.place(x=150, y=150)
    errorlabel.place(x=10, y=50)


def ChooseFolder():
    InstallLoc = filedialog.askdirectory()
    if not InstallLoc == "":
        ThirdPage()
    else:
        InstallLocCannonBeBlackError()



def gotopage3():
    InstallLoc = installlocationtextbox.get()
    if not InstallLoc == "":
        ThirdPage()
    else:
        InstallLocCannonBeBlackError()

def StartInstall():
    print("starting install")


def Abadon():
    quit()
    
    
    
    







#setting up the installer window*******************************************************************************

InstallerWin = tk.Tk()

InstallerWin.title("Amazing Hacking Tools Installer")


#size of the window
InstallerWin.geometry("500x400")
#making it NOT resizable by the user
InstallerWin.resizable(width=False, height=False)
#adding widgets
nextbutton = tk.Button(InstallerWin, text="Next", command=SecondPage, padx=15, pady=5)


selectinstalllocationbutton = tk.Button(InstallerWin, text="Choose", command=ChooseFolder, padx=30, pady=1)
SecondPageLabel = tk.Label(InstallerWin, text="Please Choose an Install Location For the Program\n and let everything else for us", font=("Arial", 15))   

welcomelabel = tk.Label(InstallerWin, text="Welcome to \n Amazing Hacking Tools \n   Installer\n press next to continue", font=("Arial", 16))
welcomelabel2 = tk.Label(InstallerWin, text="This Installer Will Help You Setup Everything in 1 Click!", font=("Arial", 10))

installlocationtextbox = tk.Entry(InstallerWin)
page2instructionslabel = tk.Label(InstallerWin, text="Enter a Install Location and press 'ok' Or click 'choose'")

okbutton = tk.Button(InstallerWin, text="Ok", font=("Arial", 12), padx=15, command=gotopage3)
yesbutton = tk.Button(InstallerWin, text="Yes", font=("Arial", 12), command=StartInstall)
nobutton = tk.Button(InstallerWin, text="No", font=("Arial", 12), command=Abadon)

areyousurelabel = tk.Label(InstallerWin, text="Start the installation?")







FirstPage()





InstallerWin.mainloop()





