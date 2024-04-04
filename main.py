from time import sleep
import os
import subprocess

loaded_assets = []

script_dir = os.path.dirname(os.path.abspath(__file__))

version = "      version = 0.1"
Logo_ascci = '''
                     _     _               _    _            _    _               _______          _
     /\             (_)   (_)             | |  | |          | |  (_)             |__   __|        | |
    /  \   _ __ ___  _ _____ _ __   __ _  | |__| | __ _  ___| | ___ _ __   __ _     | | ___   ___ | |___
   / /\ \ | '_ ` _ \| |_  / | '_ \ / _` | |  __  |/ _` |/ __| |/ / | '_ \ / _` |    | |/ _ \ / _ \| / __|
  / ____ \| | | | | | |/ /| | | | | (_| | | |  | | (_| | (__|   <| | | | | (_| |    | | (_) | (_) | \__ \
 /_/    \_\_| |_| |_|_/___|_|_| |_|\__, | |_|  |_|\__,_|\___|_|\_\_|_| |_|\__, |    |_|\___/ \___/|_|___/
                                    __/ |                                  __/ |
                                   |___/                                  |___/'''





def check_for_assets():
    print("checking for assets...")
    file_path = script_dir + "\\assets\\system\\downloader.py"
    if os.path.exists(file_path):
        print("assets found")
        print("initializing assets...")
        sleep(2)
        initialize_assets()
    else:
        print("assets not found")
        print("please download assets from github to continue...")
        print("exiting...")
        sleep(2)
        exit()

def initialize_assets():
    

    folder_path = script_dir
    files = os.listdir(folder_path)

    for file in files:
        print("hi")
        loaded_assets.append(file)
        print(loaded_assets)


    
check_for_assets()




















sleep(1)


print(Logo_ascci)

sleep(1)

print(version)



