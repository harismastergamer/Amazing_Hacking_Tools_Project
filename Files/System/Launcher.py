import tkinter as tk
import os
import requests 
from time import sleep
import subprocess

ScriptFolder = os.path.dirname(os.path.abspath(__file__))
UpdaterUrl = "https://raw.githubusercontent.com/harismastergamer/Amazing_Hacking_Tools_Project/main/Files/System/Updater.py"


def WantToLeave():
    WantToLeaveWin = tk.Tk()
    WantToLeaveWin.geometry("200x150")
    wanttoleavelabel = tk.Label(WantToLeaveWin, text="Are You Sure You Want To\nLeave?\nThis May Stop An Update\nAnd Destroy The Installation!")
    wanttoleavelabel.place(x=20, y=20)
    WantToLeaveWin.grab_set()
    yesbutton = tk.Button(WantToLeaveWin, text="Yes",command=quit)
    nobutton = tk.Button(WantToLeaveWin, text="No",command=WantToLeaveWin.destroy)
    yesbutton.place(x=150, y=120)
    nobutton.place(x=10, y=120)
    


UpdateWin = tk.Tk()
UpdateWin.geometry("300x200")
UpdateWin.title("Loading AHT")
UpdateWin.resizable(width=False, height=False)
UpdateWin.protocol("WM_DELETE_WINDOW", WantToLeave)





statuslabel = tk.Label(UpdateWin, text="Loading...", font=("Arial", 15))
statuslabel.place(relx=0.5, rely=0.2, anchor='center')
UpdateWin.update()
sleep(1)




if not os.path.exists(ScriptFolder + "/System/Updater.pyw"):
    statuslabel.config(text="Missing File - Updater.py\nDownloading...")
    UpdateWin.update()

    if not os.path.exists(ScriptFolder + "/System/"):
        os.makedirs(ScriptFolder + "/System/")
    response = requests.get(UpdaterUrl)
    if response.status_code == 200:
        with open(ScriptFolder + "/System/Updater.pyw", "wb") as updater_file:
            updater_file.write(response.content)
    else:
        statuslabel.config(text="Error Downloading Updater.py, \nPlease Check Your Internet Connection\nAnd Try Again\nExiting in 10 S...")
        UpdateWin.update()
        print("error downloading script, status_code: ", response.status_code)
        sleep(10)
        quit()
    statuslabel.config(text="Download Complete - Updater.pyw")
    UpdateWin.update()


statuslabel.config(text="Launching Updater...")
UpdateWin.update()
sleep(1)
UpdateWin.destroy()
try:
    WantToLeaveWin.destroy()
except:
    pass

if os.path.exists(ScriptFolder + "/System/InstallLoc.txt"):
    with open(ScriptFolder + "/System/ScriptFolderLoc.txt", "wb") as ScriptFolderFile:
        ScriptFolderFile.write(ScriptFolder)
        ScriptFolderFile.close()






UpdateWin.mainloop()
subprocess.Popen(["python", ScriptFolder + "/System/Updater.pyw"], creationflags=subprocess.CREATE_NEW_CONSOLE)
sleep(1)
quit()
