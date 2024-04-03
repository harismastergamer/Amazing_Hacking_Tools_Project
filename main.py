from time import sleep
import os
import subprocess
script_dir = os.path.dirname(os.path.abspath(__file__))

version = "      version = 0.1"
Logo_ascci = '''
                     _     _               _    _            _    _               _______          _     
     /\             (_)   (_)             | |  | |          | |  (_)             |__   __|        | |    
    /  \   _ __ ___  _ _____ _ __   __ _  | |__| | __ _  ___| | ___ _ __   __ _     | | ___   ___ | |___ 
   / /\ \ | '_ ` _ \| |_  / | '_ \ / _` | |  __  |/ _` |/ __| |/ / | '_ \ / _` |    | |/ _ \ / _ \| / __|
  / ____ \| | | | | | |/ /| | | | | (_| | | |  | | (_| | (__|   <| | | | | (_| |    | | (_) | (_) | \__ \\
 /_/    \_\_| |_| |_|_/___|_|_| |_|\__, | |_|  |_|\__,_|\___|_|\_\_|_| |_|\__, |    |_|\___/ \___/|_|___/
                                    __/ |                                  __/ |                         
                                   |___/                                  |___/                          '''





print(Logo_ascci)

print(version)

def startup():
    print("checking for assets...")
    if is_file_in_directory("ddos.py",script_dir):
        print("assets found")
    else:
        print("assets not found")
        print("installing assets...")
        try:
            subprocess.run(["git", "clone", "https://github.com/harismastergamer/Amazing_Hacking_Tools_Project/blob/main/assets/asset_ddos.py"])
        except:
            if input("error!n/nhave u installed git?\nwant to install now?") == "y":
                subprocess.run(["git", "install"])
            print("error installing-updating assets!\nCan't do it without git, please install manually the assets here: ")
            exit()




def main_menu():

    selection = input("1.ddos network (wifi adapter required)\ncoming soon (:\n=")
    if selection == "1":
        print("loading network ddos...")
        subprocess.run(["python", script_dir + "/ddos.py"])









def is_file_in_directory(file_path, directory_path):
    # Get the absolute paths of both the file and the directory
    abs_file_path = os.path.abspath(file_path)
    abs_directory_path = os.path.abspath(directory_path)

    # Check if the file path starts with the directory path
    return abs_file_path.startswith(abs_directory_path + os.path.sep)
    

startup()