# +-------------------------------------------------------------------------+
# | @   @ @                                 @@             @@@    @@@   @@@ |
# | @@ @@                                  @               @  @  @   @ @   @|
# | @ @ @ @ @@@@   @@@   @@@  @ @@@  @@@   @    @          @   @ @   @ @    |
# | @   @ @ @   @ @   @ @   @ @@        @ @@@  @@@  @@@@@  @   @ @   @  @@@ |
# | @   @ @ @   @ @@@@@ @     @      @@@@  @    @          @   @ @   @     @|
# | @   @ @ @   @ @     @   @ @     @   @  @    @          @  @  @   @ @   @|
# | @   @ @ @   @  @@@   @@@  @      @@@@  @     @         @@@    @@@   @@@ |
# +-------------------------------------------------------------------------+
# CopyRight(c) 2018-2025 HomingThistle3770
# All Right Reserved
# "Minecraft" is American Microsoft Corporation's name
# "DOS" is Disk Operating System
#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import os
import subprocess
import uuid
import datetime
import sys
import json
import time
import configparser
import platform
import zipfile
import socket
import base64
import webbrowser
import shutil
import urllib
from threading import Thread
def pipdown(mod):
    os.system(f"pip3 install {mod}")
    exec(f"import {mod}")
try:
    import minecraft_launcher_lib
    import wget
    import keyboard
    import requests
    from colorama import Fore, Style, init
    init(autoreset=True)
    from PIL import Image
except ModuleNotFoundError:
    pipdown("minecraft_launcher_lib")
    pipdown("wget")
    pipdown("keyboard")
    pipdown("requests")
    os.system("pip3 install colorama") #special
    from colorama import Fore, Style, init
    init(autoreset=True)
    os.system("pip3 install pillow")
    from PIL import Image

if platform.architecture()[0] == '32bit':
    print("The system is unsupport this DOS")
    exit()

def empty(*args):
    pass


__author__="HomingThistle3770"
cwd = os.getcwd()
try:
    os.makedirs(rf"{cwd}/.minecraft")
    os.makedirs(rf"{cwd}/.minecraft/assets")
    os.makedirs(rf"{cwd}/.minecraft/libraries/moe/yushi/authlib-injector")
    os.makedirs(rf"{cwd}/.minecraft/versions")
except FileExistsError:
    pass

start=time.perf_counter()
defaultMinecraftDir=rf"{cwd}/.minecraft"
conf = configparser.ConfigParser()
clientid="5c4883c1-e9c3-4469-80e3-35c9e0238103"
redirecturi="https://login.microsoftonline.com/common/oauth2/nativeclient"
authlibjson=requests.get("https://bmclapi2.bangbang93.com/mirrors/authlib-injector/artifact/latest.json").json()
authlibURL=authlibjson["download_url"]
authver=authlibjson["version"]
authlibPath=f"{cwd}/.minecraft/libraries/moe/yushi/authlib-injector/authlib-injector-{authver}.jar"
if not os.path.exists(authlibPath):
    wget.download(authlibURL,authlibPath)
MSloginData={}
YggdrasilURL="https://littleskin.cn/api/yggdrasil"
AuthlibB64=str(base64.b64encode(str(requests.get(YggdrasilURL).json()).encode('utf-8')),'utf-8')

optionstxt="""invertYMouse:false\nmouseSensitivity:0.5\nfov:0.0\ngamma:0.0\nsaturation:0.0\nrenderDistance:12\nguiScale:0\nparticles:0\nbobView:true\nmaxFps:260\ndifficulty:2\nfancyGraphics:true\nao:true\nbiomeBlendRadius:2\nrenderClouds:true\nresourcePacks:[]\nincompatibleResourcePacks:[]\nlastServer:null\nlang:en_us\nchatVisibility:0\nchatColors:true\nchatLinks:true\nchatLinksPrompt:true\nenableVsync:false\nhideServerAddress:false\nadvancedItemTooltips:false\npauseOnLostFocus:true\ntouchscreen:false\noverrideWidth:0\noverrideHeight:0\nheldItemTooltips:true\nchatHeightFocused:1.0\nchatHeightUnfocused:0.44366196\nchatScale:1.0\nchatWidth:1.0\nmipmapLevels:4\nuseNativeTransport:true\nmainHand:right\nattackIndicator:1\nnarrator:0\ntutorialStep:none\nkey_key.attack:-100\nkey_key.use:-99\nkey_key.forward:17\nkey_key.left:30\nkey_key.back:31\nkey_key.right:32\nkey_key.jump:57\nkey_key.sneak:42\nkey_key.sprint:29\nkey_key.drop:16\nkey_key.inventory:18\nkey_key.chat:20\nkey_key.playerlist:15\nkey_key.pickItem:-98\nkey_key.command:53\nkey_key.screenshot:60\nkey_key.togglePerspective:63\nkey_key.smoothCamera:0\nkey_key.fullscreen:87\nkey_key.spectatorOutlines:0\nkey_key.advancements:38\nkey_key.saveToolbarActivator:0\nkey_key.loadToolbarActivator:0\nkey_key.hotbar.1:2\nkey_key.hotbar.2:3\nkey_key.hotbar.3:4\nkey_key.hotbar.4:5\nkey_key.hotbar.5:6\nkey_key.hotbar.6:7\nkey_key.hotbar.7:8\nkey_key.hotbar.8:9\nkey_key.hotbar.9:10\nsoundCategory_master:1.0\nsoundCategory_music:1.0\nsoundCategory_record:1.0\nsoundCategory_weather:1.0\nsoundCategory_block:0.5070422\nsoundCategory_hostile:1.0\nsoundCategory_neutral:0.5\nsoundCategory_player:1.0\nsoundCategory_ambient:1.0\nmodelPart_cape:true\nmodelPart_jacket:true\nmodelPart_left_sleeve:true\nmodelPart_right_sleeve:true\nmodelPart_left_pants_leg:true\nmodelPart_right_pants_leg:true\nmodelPart_hat:true"""
def isnetconnect():
    ipaddress = socket.gethostbyname(socket.gethostname())
    if ipaddress == '127.0.0.1':
        return False
    else:
        return True
def check_disk_space():
    total, used, free = shutil.disk_usage(".")
    print(f"Total: {total // (2**30)} GiB")
    print(f"Used: {used // (2**30)} GiB")
    print(f"Free: {free // (2**30)} GiB")

# Function to show system information
def show_system_info():
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
def sysplatform():
    if sys.platform == "win32" and platform.machine() == "AMD64":
        return "windows-x64"
    elif sys.platform == "darwin" and platform.machine() == "AMD64":
        return "mac-os"
    elif sys.platform == "win32" and platform.machine() == "x86_64":
        return "windows-x64"
    elif sys.platform == "linux":
        return "linux"
    elif sys.platform == "darwin" and platform.machine() == "x86_64":
        return "mac-os"
    elif sys.platform == "win32" and platform.machine() == "aarch64":
        return "windows-arm64"
    elif sys.platform == "darwin" and platform.machine() == "aarch64":
        return "mac-os-arm64"
class neoforged:
    def fetchneoforgedlver(ver:str):
        try:
            url = f"https://bmclapi2.bangbang93.com/neoforge/list/{ver}"
            response = requests.get(url)
            vers=[]
            rawvers=[]
            if response.status_code == 200:
                for i in response.json():
                    vers.append(i['version'])
                    rawvers.append(i['rawVersion'])
                    return vers[-1]
            else:
                print("Failed to fetch Neoforge versions")
                return []
        except Exception as e:
            print(f"Error fetching Neoforge versions: {e}")
            return []
    def downloadneoforged(ver:str,java:str,Callback:dict=None):
        try:
            Callback.get("setStatus")("Downloading Neoforged installer...")
            Callback.get("setMax")(1)
            Callback.get("setProgress")(0)
            url=f"https://maven.neoforged.net/releases/net/neoforged/neoforge/neoforge-{ver}/neoforge-{ver}-installer.jar"
            if not os.path.exists(f"{defaultMinecraftDir}/neoforge-{ver}-installer.jar"):
                wget.download(url,f"{defaultMinecraftDir}/neoforge-{ver}-installer.jar")
            if not os.path.exists(os.path.join(defaultMinecraftDir,"runtime",java)):
                minecraft_launcher_lib.runtime.install_jvm_runtime(java,defaultMinecraftDir,Callback)
            Callback.get("setStatus")("Running installer")
            os.popen(f"{os.path.join(defaultMinecraftDir,"runtime",java,sysplatform(),java,"bin","java")} -jar {defaultMinecraftDir}/neoforge-{ver}-installer.jar")
            Callback.get("setStatus")("Installed")
        except Exception as e:
            print(f"Error downloading Neoforge: {e}")
            return []
class MinecraftSkins:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.load_config()
        self.skins_dir = os.path.join(os.getcwd(), ".minecraft", "skins")
        self.ensure_directories()

    def ensure_directories(self):
        """Create necessary directories if they don't exist"""
        if not os.path.exists(self.skins_dir):
            os.makedirs(self.skins_dir)

    def load_config(self):
        """Load configuration file"""
        if os.path.exists(os.path.join(defaultMinecraftDir,"config.ini")):
            self.config.read(os.path.join(defaultMinecraftDir,"config.ini"))

    def download_official_skin(self, username):
        """Download skin from official Minecraft servers"""
        try:
            print(f"{Fore.CYAN}Downloading official skin for {username}...")
            response = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}")
            if response.status_code != 200:
                print(f"{Fore.RED}Could not find player: {username}")
                return None
                
            player_uuid = response.json()['id']
            response = requests.get(f"https://sessionserver.mojang.com/session/minecraft/profile/{player_uuid}")
            if response.status_code != 200:
                print(f"{Fore.RED}Failed to fetch skin data")
                return None
                
            profile_data = response.json()
            for prop in profile_data['properties']:
                if prop['name'] == 'textures':
                    texture_data = json.loads(base64.b64decode(prop['value']))
                    skin_url = texture_data['textures']['SKIN']['url']
                    skin_response = requests.get(skin_url)
                    if skin_response.status_code == 200:
                        skin_path = os.path.join(self.skins_dir, f"{username}_official.png")
                        with open(skin_path, 'wb') as f:
                            f.write(skin_response.content)
                        print(f"{Fore.GREEN}Skin downloaded successfully to: {skin_path}")
                        return skin_path
                        
            print(f"{Fore.RED}No skin found for this player")
            return None
            
        except Exception as e:
            print(f"{Fore.RED}Error downloading official skin: {e}")
            return None

    def download_third_party_skin(self, username, server_url):
        """Download skin from third-party authentication server"""
        try:
            print(f"{Fore.CYAN}Downloading skin for {username} from {server_url}...")
            response = requests.get(f"{server_url}/sessionserver/session/minecraft/profile/{username}")
            if response.status_code != 200:
                print(f"{Fore.RED}Could not find player on third-party server: {username}")
                return None

            profile_data = response.json()
            for prop in profile_data.get('properties', []):
                if prop['name'] == 'textures':
                    texture_data = json.loads(base64.b64decode(prop['value']))
                    if 'textures' in texture_data and 'SKIN' in texture_data['textures']:
                        skin_url = texture_data['textures']['SKIN']['url']
                        skin_response = requests.get(skin_url)
                        if skin_response.status_code == 200:
                            skin_path = os.path.join(self.skins_dir, f"{username}_custom.png")
                            with open(skin_path, 'wb') as f:
                                f.write(skin_response.content)
                            print(f"{Fore.GREEN}Custom skin downloaded successfully to: {skin_path}")
                            return skin_path

            print(f"{Fore.RED}No skin found on third-party server")
            return None
            
        except Exception as e:
            print(f"{Fore.RED}Error downloading custom skin: {e}")
            return None

    def upload_skin(self, skin_path, auth_token, slim_model=False):
        """Upload skin to authenticated account"""
        try:
            print(f"{Fore.CYAN}Uploading skin...")
            if not os.path.exists(skin_path):
                print(f"{Fore.RED}Skin file not found")
                return False
                
            try:
                with Image.open(skin_path) as img:
                    width, height = img.size
                    if width != 64 or (height != 64 and height != 32):
                        print(f"{Fore.RED}Invalid skin dimensions. Must be 64x64 or 64x32")
                        return False
            except Exception as e:
                print(f"{Fore.RED}Invalid image file: {e}")
                return False

            headers = {'Authorization': f'Bearer {auth_token}'}
            files = {'file': ('skin.png', open(skin_path, 'rb'), 'image/png')}
            data = {'model': 'slim' if slim_model else 'classic'}

            response = requests.post('https://api.minecraftservices.com/minecraft/profile/skins', headers=headers, files=files, data=data)
            if response.status_code == 200:
                print(f"{Fore.GREEN}Skin uploaded successfully!")
                return True
            else:
                print(f"{Fore.RED}Failed to upload skin. Status code: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"{Fore.RED}Error uploading skin: {e}")
            return False

    def list_local_skins(self):
        """List all locally stored skins"""
        try:
            skins = [f for f in os.listdir(self.skins_dir) if f.endswith('.png')]
            if skins:
                print(f"{Fore.CYAN}Locally stored skins:")
                for skin in skins:
                    print(f"- {skin}")
                return skins
            else:
                print(f"{Fore.YELLOW}No skins found in local storage")
                return []
        except Exception as e:
            print(f"{Fore.RED}Error listing skins: {e}")
            return []

# Define the Multi-Threaded Downloader Class
class MultiThreadDownloader:
    def __init__(self, url, dest, num_threads=4):
        self.url = url
        self.dest = dest
        self.num_threads = num_threads
        self.file_size = int(requests.head(url).headers['Content-Length'])
        self.part_size = self.file_size // num_threads
        self.threads = []

    def download_part(self, part_num):
        start = part_num * self.part_size
        end = start + self.part_size - 1 if part_num < self.num_threads - 1 else self.file_size - 1
        headers = {'Range': f'bytes={start}-{end}'}
        response = requests.get(self.url, headers=headers, stream=True)
        part_file = f'{self.dest}.part{part_num}'
        with open(part_file, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        print(f"Part {part_num} downloaded")

    def combine_parts(self):
        with open(self.dest, 'wb') as f:
            for part_num in range(self.num_threads):
                part_file = f'{self.dest}.part{part_num}'
                with open(part_file, 'rb') as pf:
                    f.write(pf.read())
                os.remove(part_file)
        print(f"Download completed: {self.dest}")

    def start_download(self):
        for part_num in range(self.num_threads):
            thread = Thread(target=self.download_part, args=(part_num,))
            self.threads.append(thread)
            thread.start()
        for thread in self.threads:
            thread.join()
            self.combine_parts()

# Integrate the Downloader into the mc.py Script


class Minecraft:
    def download_file(url, dest, num_threads=4):
        downloader = MultiThreadDownloader(url, dest, num_threads)
        downloader.start_download()
    def OOO(text:str,sec:float,sleep:float):
        z=int(sec/sleep)
        for i in range(z):
            al=["-","\\","|","/"]
            ind=i%4
            print("\r{}...{}".format(text,al[ind]),end="")
            sys.stdout.flush()
            time.sleep(sleep)
    def Config_ini():
        UserUUID=uuid.uuid4()
        conf["user"]={
            "Username":"DOSCraft",
            "UUID":f"{UserUUID}",
            "Token":f"{UserUUID}",
            }
        conf["JVMMemory"]={
            "Xmx":4096
            }
        conf["userAuthlib"]={
            "Username":"DOSCraft",
            "UUID":f"{UserUUID}",
            "Token":f"{UserUUID}",
            }
        conf["userMS"]={
            "Username":"DOSCraft",
            "UUID":f"{UserUUID}",
            "Token":f"{UserUUID}",
            }
        if os.path.exists(os.path.join(defaultMinecraftDir,"config.ini")) != True:
            with open(os.path.join(defaultMinecraftDir,"config.ini"),"w") as confFile:
                conf.write(confFile)
            conf.read(os.path.join(defaultMinecraftDir,"config.ini"))
        else:
            conf.read(os.path.join(defaultMinecraftDir,"config.ini"))
    def launcher_profile():

        profile = {
            "profiles": {
                "DOSCraft": {
                    "name": "DOSCraft",
                    "gameDir": defaultMinecraftDir,
                    "lastVersionId": "1.17.1",
                    "javaDir": "java",
                    "javaArgs": "-client -Xmx4096m -Xms4096m -Xmn1536m -Xss1m -XX:-UseAdaptiveSizePolicy -XX:+UseG1GC -XX:-UseAdaptiveSizePolicy -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump",
                    "allowedReleaseTypes": ["release", "snapshot", "old_beta", "old_alpha"],
                    "launcherVisibilityOnGameClose": "keep the launcher open"
                },
                "32bit": {
                    "name": "32bit",
                    "gameDir": defaultMinecraftDir,
                    "lastVersionId": "1.8.9",
                    "javaDir": "java",
                    "javaArgs": "-client -Xmx1024m -Xms1024m -Xmn384m -Xss1m -XX:-UseAdaptiveSizePolicy -XX:+UseG1GC -XX:-UseAdaptiveSizePolicy -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump",
                    "allowedReleaseTypes": ["release", "snapshot", "old_beta", "old_alpha"],
                    "launcherVisibilityOnGameClose": "keep the launcher open"
                }
            },
            "selectedProfile": "DOSCraft",
            "clientToken": "a1b2c3d4-e5f6-a7b8-c9d0-e1f2g3h4i5j6",
            "authenticationDatabase": {
                "a1b2c3d4-e5f6-a7b8-c9d0-e1f2g3h4i5j6": {
                    "displayName": "DOSCraft",
                    "userType": "mojang",
                    "properties": []
                }
            },
            "selectedUser": "a1b2c3d4-e5f6-a7b8-c9d0-e1f2g3h4i5j6",
            "launcherVersion": {
                "name": "0.01Beta",
                "format": 21
            }
        }
        if os.path.exists(os.path.join(defaultMinecraftDir, "launcher_profiles.json")) != True:
            with open(os.path.join(defaultMinecraftDir, "launcher_profiles.json"), "w") as f:
                json.dump(profile, f, indent=4)
        else:
            pass
    def optionstxt():
        if os.path.exists(os.path.join(defaultMinecraftDir, "options.txt")) != True:
            with open(os.path.join(defaultMinecraftDir, "options.txt"), "w") as f:
                f.write(optionstxt)
    def fetch_mods_from_curseforge(api_key):
        url = "https://api.curseforge.com/v1/mods/search?gameId=432"
        headers = {
            "Accept": "application/json",
            "x-api-key": api_key
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            mods = response.json()["data"]
            return mods
        else:
            print("Failed to fetch mods from CurseForge API")
            return []
    def search_mods_from_curseforge(query, api_key):
        url = f"https://api.curseforge.com/v1/mods/search?gameId=432&searchFilter={query}"
        headers = {
            "Accept": "application/json",
            "x-api-key": api_key
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            mods = response.json()["data"]
            return mods
        else:
            print("Failed to fetch mods from CurseForge API")
            return []
    
    def ask_yes_no(text: str) -> bool:
        while True:
            answer = input(text + " [y|n]")
            if answer.lower() == "y":
                return True
            elif answer.lower() == "n":
                return False
            else:
                print("Please enter y or n")
    def skin_manager_interface(self, args=None):
        """Manage Minecraft skins"""
        while True:
            print(f"\n{Fore.CYAN}Minecraft Skin Manager")
            print("1. Download official skin")
            print("2. Download custom skin")
            print("3. Upload skin")
            print("4. List local skins")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ")
            if choice == "1":
                username = input("Enter Minecraft username: ")
                self.skin_manager.download_official_skin(username)
            elif choice == "2":
                username = input("Enter username: ")
                server = input("Enter custom server URL (press Enter for default): ")
                if server.strip():
                    self.skin_manager.download_third_party_skin(username, server)
                else:
                    self.skin_manager.download_third_party_skin(username)
            elif choice == "3":
                skin_path = input("Enter skin file path: ")
                auth_token = input("Enter authentication token: ")
                slim = Minecraft.ask_yes_no("Use slim model?")
                if slim:
                    self.skin_manager.upload_skin(skin_path, auth_token, slim)
                else:
                    self.skin_manager.upload_skin(skin_path, auth_token)
            elif choice == "4":
                self.skin_manager.list_local_skins()
            elif choice == "5":
                print(f"{Fore.CYAN}Exiting Skin Manager...")
                break
    def Menu():
        print(Fore.CYAN + "===================================================================")
        print(Fore.YELLOW + "                         Minecraft-DOS")
        print(Fore.CYAN + "===================================================================")
        print(Fore.GREEN + "Available Versions:")
        versions = minecraft_launcher_lib.utils.get_installed_versions(defaultMinecraftDir)
        if versions:
            for version in versions:
                print(Fore.WHITE + f" - {version['id']}")
        else:
            print(Fore.RED + "No versions installed.")
    def version(types):
        alllist=minecraft_launcher_lib.utils.get_version_list()
        VERSIONRel=[]
        VERSIONSna=[]
        VERSIONBeta=[]
        for abc in alllist:
            if abc["type"] == "release":
                VERSIONRel.append(abc["id"])
            elif abc["type"] == "snapshot":
                VERSIONSna.append(abc["id"])
            else:
                VERSIONBeta.append(abc["id"])
        print(Fore.CYAN + "===================================================================")
        if types == "release":
            for z in VERSIONRel:
                print(Fore.MAGENTA+f"""-{z}""")
        elif types == "snapshot":
            for s in VERSIONSna:
                print(Fore.MAGENTA+f"""-{s}""")
        else:
            for s0 in VERSIONBeta:
                print(Fore.MAGENTA+f"""-{s0}""")
        print(Fore.CYAN + "===================================================================")
    def MSLogin():
        login_url, state, code_verifier = minecraft_launcher_lib.microsoft_account.get_secure_login_data(clientid, redirecturi)
        print(f"copy the url you are redirected into the prompt below.")
        webbrowser.open(login_url)
        code_url = input()
        try:
            auth_code = minecraft_launcher_lib.microsoft_account.parse_auth_code_url(code_url, state)
        except AssertionError:
            print("States do not match!")
        except KeyError:
            print("Url not valid")
        global MSloginData
        MSloginData = minecraft_launcher_lib.microsoft_account.complete_login(clientid, None, redirecturi, auth_code, code_verifier)
    
    def javachecker(ver) -> str:
        verlist=minecraft_launcher_lib.utils.get_version_list()
        lst=[]
        jrelegacy=[]
        gamma=[]
        delta=[]
        for i in verlist:
            lst.append(i['id'])
        oldest=lst.index('rd-132211')
        java8end=lst.index('21w19a')
        java17end=lst.index('24w14a')
        jrelegacy.append(lst[oldest:java8end])
        gamma.append(lst[java8end:java17end])
        delta.append(lst[java17end:])
        if ver in jrelegacy:
            return "jre-legacy"
        elif ver in gamma:
            return "java-runtime-gamma"
        elif ver in delta:
            return "java-runtime-delta"
        else:
            return False


    class installMinecraft(Thread):
        """Install a Minecraft version.Use Minecraft.installMinecraft.Download(U Version) to download"""
        current_max=0
        statusII=""
        def set_status(status:str):
            a11=open("Status.log","a")
            a11.write(f"[A New Log]{status}\n")
            global statusII
            statusII=status

        def set_progress(progress: int):
            if current_max != 0:
                finish=int(progress/current_max*100)*"#"
                notfinish=int(100-(int(progress/current_max*100)))*"-"
                print("\r", end="")
                print(f"[{Fore.YELLOW}|{finish}=>{notfinish}|{Fore.GREEN}Downloaded:{progress}/{current_max}|{Fore.BLUE}{int(progress/current_max*100)}%|{Fore.CYAN}Task:{statusII}]", end="")
                sys.stdout.flush()

        def set_max(new_max: int):
            global current_max
            current_max = new_max

        def optifine(ver,callback:dict=None):
            """Forge+Optifine==Best group"""
            x=minecraft_launcher_lib.forge.find_forge_version(ver)
            x2=x.split("-")[1]
            callback.get("setStatus")("Searching OptiFine...")
            callback.get("setMax")(1)
            callback.get("setProgress")(0)
            optifineURL=requests.get(f"https://bmclapi2.bangbang93.com/optifine/{ver}").json()
            callback.get("setProgress")(1)
            f3=[]
            callback.get("setStatus")("Downloading OptiFine...")
            callback.get("setMax")(1)
            callback.get("setProgress")(0)
            if not optifineURL:
                print("unavaliable")
                callback.get("setStatus")("Unavaliable")
                return "Unavaliable"
            for i in optifineURL:
                if not 'pre' in i['patch']:
                    f3.append("OptiFine_{}_{}_{}.jar".format(i['mcversion'],i['type'],i['patch']))
            print("Avaliable version:{}".format(f3[-1]))
            if not os.path.exists(f"{defaultMinecraftDir}/versions/{ver}-forge-{x2}/mods"):
                os.makedirs(f"{defaultMinecraftDir}/versions/{ver}-forge-{x2}/mods")
            elif not os.path.exists(f"{defaultMinecraftDir}/versions/{ver}-forge-{x2}/mods/optifine.jar"):
                wget.download(f"https://bmclapi2.bangbang93.com/maven/com/optifine/{ver}/{f3[-1]}",f"{defaultMinecraftDir}/versions/{ver}-forge-{x2}/mods/optifine.jar")
            callback.get("setProgress")(1)
            callback.get("setStatus")("Downloaded")

        def fabricAPI(ver,callback:dict=None):
            """Fabric mods need Fabric API"""
            callback.get("setStatus")("Searching Fabric API...")
            callback.get("setMax")(1)
            callback.get("setProgress")(0)
            avver=requests.get("https://api.modrinth.com/v2/project/P7dR8mSH/version").json()
            c1=[]
            c2=[]
            for i in avver:
                if ver in i['game_versions']:
                    c1.append(i['files'][0]['url'].replace('%2B','+'))
                    c2.append(i['files'][0]['filename'])
                else:
                    return "Invalid version"
            for x in c2:
                print(c2.index(x),".",c2)
                while True:
                    try:
                        xc=int(input("Input a number"))
                        if not os.path.exists(f"{defaultMinecraftDir}/versions/fabric-loader-{ver}/mods/{c2[xc]}"):
                            wget.download(c1[xc],f"{defaultMinecraftDir}/versions/fabric-loader-{ver}/mods/{c2[xc]}")
                        break
                    except Exception as e:
                        print("ERROR:::",e)
        def sodium(ver):
            """Sodium==Optifine"""
            sover=requests.get("https://api.modrinth.com/v2/project/AANobbMI/version").json()
            s1=[]
            s2=[]
            for i in sover:
                if ver in i['game_versions'] and 'fabric' in i['loaders']:
                    s1.append(i['files'][0]['url'].replace('%2B','+'))
                    s2.append(i['files'][0]['filename'])
                else:
                    return "Invalid version"
            for x in s2:
                print(s2.index(x),".",s2)
                while True:
                    try:
                        xc=int(input("Input a number"))
                        if not os.path.exists(f"{defaultMinecraftDir}/versions/{ver}/mods/{s2[xc]}"):
                            wget.download(s1[xc],f"{defaultMinecraftDir}/versions/{ver}/mods/{s2[xc]}")
                        break
                    except Exception as e:
                        return "ERROR:::"+e         
        def Download(ver,args=None):
            """TODo..."""
            callback={"setStatus":Minecraft.installMinecraft.set_status,"setProgress":Minecraft.installMinecraft.set_progress,"setMax":Minecraft.installMinecraft.set_max}
            if args:
                args2=args.split(" ")
                if "--forge" in args2:
                    if "--optifine" in args2:
                        if minecraft_launcher_lib.forge.find_forge_version(ver) != None:
                            minecraft_launcher_lib.forge.install_forge_version(minecraft_launcher_lib.forge.find_forge_version(ver),defaultMinecraftDir,callback=callback)
                            print(f"\nSuccess Install Forge {minecraft_launcher_lib.forge.find_forge_version(ver)}")
                            Minecraft.installMinecraft.optifine(ver)
                        else:
                            print("Unsupport version",ver)
                    else:
                        if minecraft_launcher_lib.forge.find_forge_version(ver) != None:
                            minecraft_launcher_lib.forge.install_forge_version(minecraft_launcher_lib.forge.find_forge_version(ver),defaultMinecraftDir,callback=callback)
                            print(f"\nSuccess Install Forge {minecraft_launcher_lib.forge.find_forge_version(ver)}")
                        else:
                            print("Unsupport version",ver)
                elif "--fabric" in args2:
                    if "--sodium" in args2:
                        if minecraft_launcher_lib.fabric.is_minecraft_version_supported(ver):
                            minecraft_launcher_lib.fabric.install_fabric(ver, defaultMinecraftDir, callback=callback)
                            print(f"\nSuccess Install {ver}")
                            Minecraft.installMinecraft.fabricAPI(ver)
                            Minecraft.installMinecraft.sodium(ver)
                        else:
                            print("Unsupport version",ver)
                    else:
                        if minecraft_launcher_lib.fabric.is_minecraft_version_supported(ver):
                            minecraft_launcher_lib.fabric.install_fabric(ver, defaultMinecraftDir, callback=callback)
                            print(f"\nSuccess Install {ver}")
                            Minecraft.installMinecraft.fabricAPI(ver)
                        else:
                            print("Unsupport version",ver)
                elif "--quilt" in args2:
                    if minecraft_launcher_lib.quilt.is_minecraft_version_supported(ver):
                        minecraft_launcher_lib.quilt.install_quilt(ver,defaultMinecraftDir,callback=callback)
                        print(f"\nSuccess Install {ver}")
                    else:
                        print("Unsupport version",ver)
                elif "--neoforge" in args2:
                    if neoforged.fetchneoforgedlver:
                        neoforged.downloadneoforged(ver,neoforged.fetchneoforgedlver(ver),callback)
                    else:
                        print("Unsupport Version",ver)
                elif "--vanilla" in args2:
                    minecraft_launcher_lib.install.install_minecraft_version(ver, defaultMinecraftDir, callback=callback)
                    print(f"\nSuccess Install {ver}")
                elif "--help" in args2:
                    print(f"""{Fore.YELLOW}ARGS DOCUMATION
{Fore.CYAN}+------------------------------------------+
{Fore.GREEN}| --forge[--optifine]                      |
{Fore.WHITE}| Install Forge[and optifine]              |
{Fore.CYAN}+------------------------------------------+
{Fore.GREEN}| --fabric[--sodium]                       |
{Fore.WHITE}| Install Fabric+API[and sodium]           |
{Fore.CYAN}+------------------------------------------+
{Fore.GREEN}| --quilt                                  |
{Fore.WHITE}| Install Quilt                            |
{Fore.CYAN}+------------------------------------------+
{Fore.GREEN}| --neoforge                               |
{Fore.WHITE}| Install Neoforged                        |
{Fore.CYAN}+------------------------------------------+
{Fore.GREEN}| --vanilla                                |
{Fore.WHITE}| Install Vanilla                          |
{Fore.CYAN}+------------------------------------------+
{Fore.GREEN}| --help                                   |
{Fore.WHITE}| Help documents                           |
{Fore.CYAN}+------------------------------------------+""")
                else:
                    print(f"{Fore.RED}Input `--help` to help")
            else:
                try:
                    while True:
                        ifmodload=input("Select modloader:\nfo.Forge\nfa.Fabric\nq.quilt\nv.vanilla\n0.no install\n>>>")
                        if ifmodload.lower() == "fo":
                            if minecraft_launcher_lib.forge.find_forge_version(ver) != None:
                                minecraft_launcher_lib.forge.install_forge_version(minecraft_launcher_lib.forge.find_forge_version(ver),defaultMinecraftDir,callback=callback)
                                print(f"\nSuccess Install Forge {minecraft_launcher_lib.forge.find_forge_version(ver)}")
                                if Minecraft.ask_yes_no("Download optifine?>>>"):
                                    Minecraft.installMinecraft.optifine(ver)
                                    break
                                else:
                                    break
                            else:
                                print("Unsupport version",ver)
                        elif ifmodload.lower() == "fa":
                            if minecraft_launcher_lib.fabric.is_minecraft_version_supported(ver):
                                minecraft_launcher_lib.fabric.install_fabric(ver, defaultMinecraftDir, callback=callback)
                                print(f"\nSuccess Install {ver}")
                                if Minecraft.ask_yes_no("Download fabric api and sodium?>>>"):
                                    Minecraft.installMinecraft.fabricAPI(ver)
                                    Minecraft.installMinecraft.sodium(ver)
                                    break
                                else:
                                    break
                            else:
                                print("Unsupport version",ver)
                        elif ifmodload.lower() == "q":
                            if minecraft_launcher_lib.quilt.is_minecraft_version_supported(ver):
                                minecraft_launcher_lib.quilt.install_quilt(ver,defaultMinecraftDir,callback=callback)
                                print(f"\nSuccess Install {ver}")
                                break
                            else:
                                print("Unsupport version",ver)
                        elif ifmodload.lower() == "v":
                            minecraft_launcher_lib.install.install_minecraft_version(ver, defaultMinecraftDir, callback=callback)
                            print(f"\nSuccess Install {ver}")
                            break
                        elif ifmodload == "0":
                            break
                        else:
                            print("Input fo/fa/q/v or 0")
                except Exception as e:
                    print("FOUND A ERROR:",e)
        class installMrpack(Thread):
            def mrpackinfor(path):
                information = minecraft_launcher_lib.mrpack.get_mrpack_information(path)
                print(f"Name: {information['name']}")
                print(f"Summary: {information['summary']}")
            def mrpackinstall(path):
                callback={"setStatus":Minecraft.installMinecraft.set_status,"setProgress":Minecraft.installMinecraft.set_progress,"setMax":Minecraft.installMinecraft.set_max}
                minecraft_launcher_lib.mrpack.install_mrpack(path, defaultMinecraftDir, callback=callback)
    def uninstall_minecraft_version(version):
        version_dir = os.path.join(".minecraft", "versions", version)
        if os.path.exists(version_dir):
            shutil.rmtree(version_dir)
            print(f"Uninstalled Minecraft version: {version}")
        else:
            print(f"Version {version} not found.")
    def download_mod(mod_name, game_version):
        conf = configparser.ConfigParser()
        conf.read(os.path.join(defaultMinecraftDir,"config.ini"))
        api_key = conf.get("api", "CurseForgeAPIKey", fallback=None)
        if not api_key:
            print("CurseForge API key not found in config.ini.")
            return ""
        headers = {"x-api-key": api_key}
        search_url = f"https://api.curseforge.com/v1/mods/search?gameId=432&searchFilter={mod_name}"
        response = requests.get(search_url, headers=headers)
        if response.status_code != 200:
            print("Failed to search for mod.")
            return
        mods = response.json()["data"]
        if not mods:
            print("No mods found.")
            return
        # Select the first mod for simplicity
        mod_id = mods[0]["id"]
        files_url = f"https://api.curseforge.com/v1/mods/{mod_id}/files"
        response = requests.get(files_url, headers=headers)
        if response.status_code != 200:
            print("Failed to fetch mod files.")
            return
        files = response.json()["data"]
        compatible_files = [file for file in files if game_version in file["gameVersions"]]
        if not compatible_files:
            print("No compatible files found for the specified game version.")
            return
        # Select the first compatible file for simplicity
        file_url = compatible_files[0]["downloadUrl"]
        mods_dir = os.path.join(".minecraft", "mods")
        os.makedirs(mods_dir, exist_ok=True)
        dest_path = os.path.join(mods_dir, f"{mod_name}.jar")
        wget.download(file_url, dest_path)
        print(f"Downloaded mod {mod_name} for Minecraft {game_version}.")
    class RunMinecraft(Thread):
        def log4j(ver):
            log4jconfig = """<Configuration status="WARN">
    <Appenders>
        <Console name="SysOut" target="SYSTEM_OUT">
            <PatternLayout pattern="[%d{HH:mm:ss}] [%t/%level]: %msg{nolookups}%n"/>
        </Console>
        <Queue name="ServerGuiConsole">
            <PatternLayout pattern="[%d{HH:mm:ss} %level]: %msg{nolookups}%n"/>
        </Queue>
        <RollingRandomAccessFile name="File" fileName="logs/latest.log" filePattern="logs/%d{yyyy-MM-dd}-%i.log.gz">
            <PatternLayout pattern="[%d{HH:mm:ss}] [%t/%level]: %msg{nolookups}%n"/>
            <Policies>
                <TimeBasedTriggeringPolicy/>
                <OnStartupTriggeringPolicy/>
            </Policies>
        </RollingRandomAccessFile>
    </Appenders>
    <Loggers>
        <Root level="info">
            <filters>
                <MarkerFilter marker="NETWORK_PACKETS" onMatch="DENY" onMismatch="NEUTRAL"/>
            </filters>
            <AppenderRef ref="SysOut"/>
            <AppenderRef ref="File"/>
        </Root>
    </Loggers>
</Configuration>"""
            if os.path.exists(f"{defaultMinecraftDir}/versions/{ver}/log4j2.xml") != True:
                with open(f"{defaultMinecraftDir}/versions/{ver}/log4j2.xml", "w") as f:
                    f.write(log4jconfig)
        """Use Minecraft.RunMinecraft.Run(U Version,Username,UUID,Token,Memory) to run"""
        def Run(ver, username, uuid, token, Xmx:int, authlib=False,args:list=None):
            """__TODo__"""
            try:
                options = minecraft_launcher_lib.utils.generate_test_options()
                options["launcherName"] = "Minecraft-DOS"
                options["launcherVersion"]="0.01Beta"
                options["username"]=username
                options["uuid"]=uuid
                options["token"]=token
                options["-d64"]=True
                options["gameDirectory"] = f"{cwd}/.minecraft/versions/{ver}"
                options["jvmArguments"] = ["-client",f"-Xmx{Xmx}m",f"-Xms{Xmx}m","-Xss1m",'-XX:+UnlockExperimentalVMOptions', '-XX:+UseG1GC', '-XX:G1NewSizePercent=20', '-XX:G1ReservePercent=20', '-XX:MaxGCPauseMillis=50', '-XX:G1HeapRegionSize=32m', '-XX:-UseAdaptiveSizePolicy', '-XX:-OmitStackTraceInFastThrow', '-XX:-DontCompileHugeMethods', '-Dfml.ignoreInvalidMinecraftCertificates=true', '-Dfml.ignorePatchDiscrepancies=true', '-XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump']
                if authlib:
                    options["jvmArguments"].append(f"-javaagent:{authlibPath}={YggdrasilURL}")
                    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(ver, defaultMinecraftDir , options)
                    minecraft_command.insert(minecraft_command.index(f"-javaagent:{authlibPath}={YggdrasilURL}")+1,"-Dauthlibinjector.side:client")
                    minecraft_command.insert(minecraft_command.index(f"-javaagent:{authlibPath}={YggdrasilURL}")+2,f"-Dauthlibinjector.yggdrasil.prefetched:{AuthlibB64}")
                elif args:
                    options["jvmArguments"]=args
                else:
                    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(ver, defaultMinecraftDir , options)
                print("Spawned Launcher CMD")
                print(f"Run Minecraft With {minecraft_command}")
                print("""DOS/4GW Protected Mode Runtime Version 1.97\nCopyright(c)Rational Systems, Inc. 1990-1994\n\nLoading MineCraft 3D\n(c)1991-2024 Mojang PC Repair and Software AB\n\nLoading MINECRAFT.JAR""")
                print("""
==============================================================================
Minecraft Log
==============================================================================
""")
                subprocess.call(minecraft_command)
                print("EXIT")
            except minecraft_launcher_lib.exceptions.VersionNotFound:
                if Minecraft.ask_yes_no("Do you want install the version"):
                    Minecraft.installMinecraft.Download(ver)
            except Exception as e:
                print("ERROR!",e)
    def ConfPanel():
        conf = configparser.ConfigParser()
        global defaultMinecraftDir
        conf.read(os.path.join(defaultMinecraftDir,"config.ini"))
        global YggdrasilURL
        while True: 
            print(Fore.CYAN + "\nCONFIG PANEL")
            print(Fore.CYAN + "========================")
            print(Fore.CYAN + "Current Settings:")
            print(Fore.YELLOW + f"1. Username: {conf['user']['Username']}")
            print(Fore.YELLOW + f"2. Memory (Xmx): {conf['JVMMemory']['Xmx']} MB")
            print(Fore.YELLOW + f"3. Authlib URL: {YggdrasilURL}")
            print(Fore.YELLOW + f"4. Minecraft-Path: {defaultMinecraftDir}")
            print(Fore.YELLOW + f"5. Exit")
            print(Fore.CYAN + "========================")
            choice = input(Fore.CYAN + "Choose an option to change (1-5): ").strip()
            if choice == "1":
                new_username = input(Fore.CYAN + "Enter new username (or 'exit0' to cancel): ").strip()
                if new_username != "exit0":
                    conf["user"]["Username"] = new_username
                    print(Fore.GREEN + f"Username changed to {new_username}")
            elif choice == "2":
                try:
                    new_memory = int(input(Fore.CYAN + "Enter new memory (MB) (or '0' to cancel): ").strip())
                    if new_memory > 0:
                        conf["JVMMemory"]["Xmx"] = str(new_memory)
                        print(Fore.GREEN + f"Memory (Xmx) changed to {new_memory} MB")
                    elif new_memory == 0:
                        print(Fore.YELLOW + "Memory change canceled")
                    else:
                        print(Fore.RED + "Invalid memory value")
                except ValueError:
                    print(Fore.RED + "Invalid input. Please enter a valid number.")
            elif choice == "3":
                new_url = input(Fore.CYAN + "Enter new Authlib URL (or 'exit0' to cancel): ").strip()
                if new_url != "exit0":
                    try:
                        urllib.request.urlopen(new_url)
                        YggdrasilURL = new_url
                        print(Fore.GREEN + f"Authlib URL changed to {new_url}")
                    except ValueError:
                        print(Fore.RED + "Invalid URL")
                    except Exception as e:
                        print(Fore.RED + f"Error: {e}")
            elif choice == "4":
                newdir = input(Fore.CYAN + "Enter new Path (or 'exit0' to cancel,REQUIED EXISTS AND FULL!!!): ").strip()
                if new_url != "/exit0":
                    if os.path.isdir(newdir):
                        defaultMinecraftDir=newdir
                    else:
                        print(Fore.RED + "PATH ERROR OR NOT EXISTS")
            elif choice == "5":
                print(Fore.CYAN + "Exiting configuration panel...")
                break
            else:
                print(Fore.RED + "Invalid choice. Please select a valid option.")
            # Save changes to config.ini
            with open(os.path.join(defaultMinecraftDir,"config.ini"), "w") as configfile:
                conf.write(configfile)
            print(Fore.GREEN + "Changes saved.")
    def fetch_mods_from_modrinth():
        url = "https://api.modrinth.com/v2/search"
        headers = {
            "limit": "1000",
            "facets": "[[\"project_type\",\"mod\"]]",
            }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            mods = response.json()['hits']
            return mods
        else:
            print("Failed to fetch mods from Modrinth API")
            return []

    def search_mods_from_modrinth(query):
        url = f"https://api.modrinth.com/v2/search?query={query}"
        headers = {
            "limit": "1000",
            "facets": "[[\"project_type\",\"mod\"]]",
            }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            mods = response.json()['hits']
            return mods
        else:
            print("Failed to fetch mods from Modrinth API")
            return []
    @staticmethod
    def download_mod_from_modrinth(mod_id, game_version):
        url = f"https://api.modrinth.com/v2/project/{mod_id}/version"
        response = requests.get(url)
        if response.status_code != 200:
            print("Failed to fetch mod versions from Modrinth API")
            return

        versions = response.json()
        compatible_versions = [v for v in versions if game_version in v["game_versions"] and v["version_type"] == "release"]
        if not compatible_versions:
            print("No compatible versions found for the specified game version.")
            return

        download_url = compatible_versions[0]["files"][0]["url"]
        mods_dir = os.path.join(".minecraft", "mods")
        os.makedirs(mods_dir, exist_ok=True)
        dest_path = os.path.join(mods_dir, f"{mod_id}.jar")
        wget.download(download_url, dest_path)
        print(f"Downloaded mod {mod_id} for Minecraft {game_version}.")

    def AuthlibSign(URL,Username,Password):
        AuthlibJson={
            "username":Username,
            "password":Password,
            "agent":{
                "name":"Minecraft",
                "version":1
                }
            }
        requestJson=requests.post(URL+"/authserver/authenticate",json=AuthlibJson).json()
        if not 'error' in requestJson:
            conf = configparser.ConfigParser()
            conf.read(os.path.join(defaultMinecraftDir,"config.ini"))
            conf["userAuthlib"]["Username"] = requestJson["selectedProfile"]["name"]
            conf["userAuthlib"]["UUID"]=requestJson["selectedProfile"]["id"]
            conf["userAuthlib"]["Token"]=requestJson["accessToken"]
            with open(os.path.join(defaultMinecraftDir,"config.ini"), "w") as configfile:
                conf.write(configfile)
        else:
            print("ERROR:",requestJson["errorMessage"])
    def copyrightandthanks(xc):
        x="""Minecraft-DOS
Version:0.01Beta
Author:HomingThistle3770
Thanks to:
-minecraft_launcher_lib
-requests
-colorama
-wget
-urllib
-mojang
-Modrinth
-CurseForge
-OptiFine
-Sodium
-Fabric
-Forge
-Quilt
-Authlib-Injector
-Microsoft
-Github Copilot:)"""     
        x2="""Copyright:
Minecraft-DOS (0.01Beta) 
(c)2021-2025 HomingThistle3770  All rights reserved.

Python 3.13.1
(c)1991-2025 Python Software Foundation - Guido van Rossum. All rights reserved.

Minecraft
(c)2009-2025 Mojang AB. Do not distribute.

MS-DOS
(c)1975-2025 Microsoft Corporation. All rights reserved.

Github Copilot
(c)2021-2025 Github Inc. All rights reserved.
"""
        if xc == 'COPYRIGHT':
            return x2
        elif xc == 'THANKS':
            return x
        else:
            return x+"\n\n"+x2
    def DOS():
        conf = configparser.ConfigParser()
        conf.read(os.path.join(defaultMinecraftDir,"config.ini"))
        username1=conf["user"]["Username"]
        uuid1=conf["user"]["UUID"]
        token1=conf["user"]["Token"]
        Xmx1=conf["JVMMemory"]["Xmx"]
        api_key = "$2a$10$6.P/W1SuOQxOsPnsqHYHc.01wQN.duMd2nxrYwOJJCP4nKhLXEdza"
        helpf=f"""
{Fore.YELLOW}Minecraft-DOS Help documents
{Fore.CYAN}----------------------------------------------------
{Fore.GREEN}listver{Fore.WHITE} (None)
{Fore.WHITE}List all version
{Fore.CYAN}----------------------------------------------------
{Fore.GREEN}download{Fore.WHITE} (Vers)
{Fore.WHITE}Download a version
{Fore.CYAN}----------------------------------------------------
{Fore.GREEN}launch{Fore.WHITE} (Vers)
{Fore.WHITE}Launch a version
{Fore.CYAN}----------------------------------------------------
{Fore.GREEN}config{Fore.WHITE} (None)
{Fore.WHITE}Configure your profile
{Fore.CYAN}----------------------------------------------------
{Fore.GREEN}clear{Fore.WHITE} (None)
{Fore.WHITE}Clear Console
{Fore.CYAN}----------------------------------------------------
{Fore.GREEN}refrver{Fore.WHITE} or {Fore.GREEN}F5{Fore.WHITE} (None)
{Fore.WHITE}Refresh installed versions
{Fore.CYAN}----------------------------------------------------
{Fore.GREEN}mslogin{Fore.WHITE} (None)
{Fore.WHITE}Microsoft Login
{Fore.CYAN}----------------------------------------------------
{Fore.GREEN}authlib{Fore.WHITE} (None)
{Fore.WHITE}Authlib-Injector Yggdrasil Sign
{Fore.CYAN}----------------------------------------------------
{Fore.GREEN}alaunch{Fore.WHITE} (Vers)
{Fore.WHITE}Authlib-Injector Launch
{Fore.CYAN}----------------------------------------------------
{Fore.GREEN}mslaunch{Fore.WHITE} (Vers)
{Fore.WHITE}Microsoft Account Launch
{Fore.CYAN}----------------------------------------------------
{Fore.GREEN}modsmenu {Fore.WHITE}(None)(Beta)
{Fore.WHITE}Display available mods from CurseForge API
{Fore.CYAN}----------------------------------------------------
{Fore.GREEN}checkdisk {Fore.WHITE}(None)
{Fore.WHITE}Check available disk space
{Fore.CYAN}----------------------------------------------------
{Fore.GREEN}sysinfo {Fore.WHITE}(None)
{Fore.WHITE}Show system information
{Fore.CYAN}----------------------------------------------------
{Fore.GREEN}uninstall {Fore.WHITE}(Vers)
{Fore.WHITE}Uninstall a Minecraft version
{Fore.CYAN}----------------------------------------------------
{Fore.GREEN}modmenu {Fore.WHITE}(Beta)
{Fore.WHITE}Fetch mods from CurseForge
{Fore.CYAN}----------------------------------------------------
{Fore.GREEN}searchmod {Fore.WHITE}(None)
{Fore.WHITE}Search mods from CurseForge API
{Fore.CYAN}----------------------------------------------------
{Fore.GREEN}downmod {Fore.WHITE}(ModName GameVersion)(Beta)
{Fore.WHITE}Download a mod from CurseForge
{Fore.CYAN}----------------------------------------------------
{Fore.GREEN}modrinth{Fore.WHITE} (None)
{Fore.WHITE}Display available mods from Modrinth API
{Fore.CYAN}----------------------------------------------------
{Fore.GREEN}downmodrinth{Fore.WHITE} (ModID GameVersion)
{Fore.WHITE}Download a mod from Modrinth
{Fore.CYAN}----------------------------------------------------
{Fore.GREEN}skinmanager{Fore.WHITE} (None)
{Fore.WHITE}Manage Minecraft skins
{Fore.CYAN}----------------------------------------------------
{Fore.GREEN}searchmodrinth{Fore.WHITE} (None)
{Fore.WHITE}Search mods from Modrinth API
{Fore.CYAN}----------------------------------------------------
{Fore.GREEN}exit{Fore.WHITE} (None)
{Fore.WHITE}Exit Minecraft-DOS
{Fore.CYAN}----------------------------------------------------
"""        
        print(Fore.CYAN + "Enter `help` for help")
        while True:
            try:
                DOS = input(f"{cwd}:>>> ")
                parts = DOS.split(" ")
                if parts[0] == 'download':
                    if len(parts) > 2:
                        Vers = parts[1]
                        if parts[2] == "Shareware":
                            print("Please use `download 3d_shareware` instead `download 3D Shareware v1.34`.")
                        else:
                            Minecraft.installMinecraft.Download(Vers,DOS.replace(f"download {Vers} ",""))
                    elif len(parts) == 2:
                        Vers = parts[1]
                        if Vers == "3d_shareware":
                            Vers = "3D Shareware v1.34"
                        Minecraft.installMinecraft.Download(Vers)
                    else:
                        print("Incorrect")
                elif parts[0] == 'launch':
                    version = parts[1]
                    if len(parts) > 2:
                        args=parts[2:]
                        if '-u' in args and '--custom-args' not in args:
                            username=args[args.index('-u')+1]
                            Minecraft.RunMinecraft.Run(version, username, uuid1, token1, Xmx1)
                        elif '--custom-args' in args and '-u' not in args:
                            customarg=args[args.index('--custom-args')+1:]
                            username=username1
                            Minecraft.RunMinecraft.Run(version, username, uuid1, token1, Xmx1, args=customarg)
                        elif '--custom-args' in args and '-u' in args:
                            customarg=args[args.index('--custom-args')+1:]
                            username=args[args.index('-u')+1]
                            Minecraft.RunMinecraft.Run(version, username, uuid1, token1, Xmx1, args=customarg)
                        else:
                            username=username1
                            Minecraft.RunMinecraft.Run(version,username,uuid1,token1,Xmx1)
                    else:
                        username=username1
                        Minecraft.RunMinecraft.Run(version,username,uuid1,token1,Xmx1)
                elif parts[0] == "config":
                    Minecraft.ConfPanel()
                elif parts[0] == "modsmenu":
                    mods = Minecraft.fetch_mods_from_curseforge(api_key)
                    if mods:
                        print("Available Mods from CurseForge:")
                        for mod in mods:
                            print(f"- {mod['name']} ({mod['slug']})")
                elif parts[0] == "searchmod":
                    query = input("Enter search query: ")
                    mods = Minecraft.search_mods_from_curseforge(query, api_key)
                    if mods:
                        print("Search results:")
                        for mod in mods:
                            print(f"- {mod['name']} ({mod['slug']})")
                elif parts[0] == "checkdisk":
                    check_disk_space()
                elif parts[0] == "sysinfo":
                    show_system_info()
                elif parts[0] == "pythonsfather":
                    print("Guido van Rossum")
                elif parts[0] == "uninstall":
                    ver=parts[1]
                    Minecraft.uninstall_minecraft_version(ver)
                elif parts[0] == 'modmenu':
                    Minecraft.fecth_mods_from_curseforge(api_key)
                elif parts[0] == "listver":
                    print(Fore.CYAN + "List versions\nTypes:\n(1)Release\n(2)Snapshot\n(3)Old Alpha\n(4)Exit\n(Can Multi choose)")
                    while True:
                        listVer=input("Choice a types of versions>>>")
                        if "1" in listVer:
                            Minecraft.version('release')
                            break
                        elif "2" in listVer:
                            Minecraft.version('snapshot')
                            break
                        elif "3" in listVer:
                            Minecraft.version('oldalpha')
                            break
                        elif "4" in listVer:
                            break
                        else:
                            print("invalid")
                elif parts[0] == "mslogin":
                    Minecraft.MSLogin()
                    conf = configparser.ConfigParser()
                    conf.read(os.path.join(defaultMinecraftDir,"config.ini"))
                    conf["userMS"]["Username"] = MSloginData["name"]
                    conf["userMS"]["UUID"]=MSloginData["id"]
                    conf["userMS"]["Token"]=MSloginData["access_token"]
                    with open(os.path.join(defaultMinecraftDir,"config.ini"), "w") as configfile:
                        conf.write(configfile)
                elif parts[0] == 'mslaunch':
                    Vers21=parts[1]
                    if '--custom-args' in parts:
                        args=parts[parts.index('--custom-args')+1:]
                    else:
                        args=[]
                    conf = configparser.ConfigParser()
                    conf.read(os.path.join(defaultMinecraftDir,"config.ini"))
                    Minecraft.RunMinecraft.Run(Vers21,conf["userMS"]["Username"],conf["userMS"]["UUID"],conf["userMS"]["Token"],Xmx1,args=args if args != [] else None)
                elif parts[0] == "cat":
                    if len(parts) >= 2:
                        print(open(DOS.replace("cat ","")).read())
                    else:
                        print("INVALID SYNTAX")
                elif parts[0] == "authlib":
                    if len(parts) > 1:
                        args=parts[1:]
                        if '-e' in args and '-p' in args:
                            email=args[args.index('-e')+1]
                            passwd=args[args.index('-p')+1]
                        elif '-e' in args and '-p' not in args:
                            email=args[args.index('-e')+1]
                            passwd=input("Password:")
                        elif '-p' in args and '-e' not in args:
                            email=input("Email:")
                            passwd=args[args.index('-p')+1]
                        elif '-h' in args or '-?' in args:
                            print(f"{Fore.CYAN}ARGS Help doc\n+------------------------------------------------------+\n| '-e <somename@example.com>'            Your Email    |\n| '-p <password>'                        Your Password |\n| '-h' or '-?'                           Help Docs     |\n+------------------------------------------------------+")
                    else:
                        email = input("Email:")
                        passwd = input("Password:")
                    Minecraft.AuthlibSign(YggdrasilURL, email, passwd)
                elif parts[0] == 'alaunch':
                    Vers21=parts[1]
                    if '--custom-args' in parts:
                        args=parts[parts.index('--custom-args')+1:]
                    else:
                        args=[]
                    conf = configparser.ConfigParser()
                    conf.read(os.path.join(defaultMinecraftDir,"config.ini"))
                    Minecraft.RunMinecraft.Run(Vers21,conf["userAuthlib"]["Username"],conf["userAuthlib"]["UUID"],conf["userAuthlib"]["Token"],Xmx1,authlib=True,args=args if args != [] else None)
                elif parts[0] == 'skinmanager':
                    Minecraft.skin_manager_interface()
                elif parts[0] == "echo":
                    if len(parts) >= 2:
                        print(DOS.replace("echo ",""))
                elif parts[0] == "help":
                    print(helpf)
                elif parts[0] == "downmodrinth":
                    if len(parts) == 3:
                        mod_id = parts[1]
                        game_version = parts[2]
                        Minecraft.download_mod_from_modrinth(mod_id, game_version)
                    else:
                        print("Usage: downmodrinth <ModID> <GameVersion>")
                elif parts[0] == "modrinth":
                    mods = Minecraft.fetch_mods_from_modrinth()
                    if mods:
                        print("Available Mods from Modrinth:")
                        for mod in mods:
                            print(f"- {mod['title']} ({mod['slug']})")
                elif parts[0] == "searchmodrinth":
                    if len(parts) == 1:
                        query = input("Enter search query: ")
                    elif len(parts) == 2:
                        query = parts[1]
                    else:
                        print("Invalid syntax. Usage: searchmodrinth [query] or searchmodrinth")
                        continue
                    mods = Minecraft.search_mods_from_modrinth(query)
                    if mods:
                        print("Search results:")
                        for mod in mods:
                            print(f"- {mod['title']} ({mod['slug']})")
                elif parts[0] == "clear":
                    print("\033c",end="")
                elif parts[0] == "refrver" or keyboard.is_pressed("f5"):
                    versions = minecraft_launcher_lib.utils.get_installed_versions(defaultMinecraftDir)
                    if versions:
                        for version in versions:
                            print(f" - {version['id']}")
                    else:
                        print("No versions installed.")
                    time.sleep(0.5)
                elif DOS == "":
                    pass
                elif parts[0] == "downmod":
                    if len(parts) == 3:
                        mod_name = parts[1]
                        game_version = parts[2]
                        Minecraft.download_mod(mod_name, game_version)
                    else:
                        print("Usage: downmod <ModName> <GameVersion>")
                elif parts[0] == "command":
                    if parts[1] == "run":
                        if parts[2] == "py":
                            exec(str(parts[3:]).replace("[","").replace("]","").replace(", "," ").replace("'","").replace('"',""))
                        elif parts[2] == "shell":
                            os.system(str(parts[3:]).replace("[","").replace("]","").replace(", "," ").replace("'","").replace('"',""))
                    elif parts[1] == "sh":
                        if sys.platform == "win32":
                            os.system("cmd")
                        elif sys.platform == "darwin":
                            os.system("zsh" if os.path.exists("/bin/zsh") else "bash")
                        else:
                            os.system("bash")
                    elif parts[1] == "help":
                        print(rf"""{Fore.BLUE}
`command` docs
`command` [run|sh|help] [py|shell]
        run           RUN COMMANDS
            py        EXEC PYTHONCOMMANDS
            shell     EXEC CMD
        sh            BASHES
        help          DOCS""")
                    else:
                        print(Fore.RED+"Invalid,Enter `command help` to help")
                elif parts[0] == "python3":
                    if len(parts) == 2:
                        exec(open(parts[1]).read())
                    elif len(parts) > 2:
                        os.system(f"python3 {parts[1]} {str(parts[2:]).replace('[','').replace(']','').replace(', ','').replace("'","").replace('"','')}")
                    else:
                        exec(input(">>>"))
                elif parts[0] == "cd":
                    if len(parts) < 1:
                        print(Fore.RED + "Invalid syntax. Usage: cd <directory>")
                    elif len(parts) >= 2:
                        try:
                            os.chdir(DOS.replace("cd ",""))
                        except Exception as e:
                            print("ERROR:",e)
                    else:
                        try:
                            os.chdir(parts[1])
                        except Exception as e:
                            print("ERROR:",e)
                elif parts[0] == "mkdir":
                    if len(parts) < 1:
                        print(Fore.RED + "Invalid syntax. Usage: mkdir <directory>")
                    elif len(parts) >= 2:
                        try:
                            os.makedirs(DOS.replace("mkdir ",""))
                        except Exception as e:
                            print("ERROR:",e)
                    else:
                        try:
                            os.makedirs(parts[1])
                        except Exception as e:
                            print("ERROR:",e)
                elif parts[0] == "rmdir":
                    if len(parts) < 1:
                        print(Fore.RED + "Invalid syntax. Usage: rmdir <directory>")
                    elif len(parts) >= 2:
                        try:
                            os.rmdir(DOS.replace("rmdir ",""))
                        except Exception as e:
                            print("ERROR:",e)
                    else:
                        try:
                            os.rmdir(parts[1])
                        except Exception as e:
                            print("ERROR:",e)
                elif parts[0] == "del":
                    if len(parts) < 1:
                        print(Fore.RED + "Invalid syntax. Usage: del <file>")
                    elif len(parts) >= 2:
                        try:
                            os.remove(DOS.replace("del ",""))
                        except Exception as e:
                            print("ERROR:",e)
                    else:
                        try:
                            os.remove(parts[1])
                        except Exception as e:
                            print("ERROR:",e)
                elif os.path.exists(parts[0]) and parts[0].endswith(".bat"):
                    os.system(DOS)
                elif os.path.exists(parts[0]) and parts[0].endswith(".exe"):
                    os.system(DOS)
                elif parts[0] == "rm":
                    if len(parts) < 1:
                        print(Fore.RED + "Invalid syntax. Usage: rm <file>")
                    elif len(parts) >= 2:
                        try:
                            os.remove(DOS.replace("rm ",""))
                        except Exception as e:
                            print("ERROR:",e)
                    else:
                        try:
                            os.remove(parts[1])
                        except Exception as e:
                            print("ERROR:",e)
                elif parts[0] == 'exit':
                    sys.exit(0)
                elif ['fuck','shit','nigger'] in DOS.lower():
                    print(Fore.RED+f"FATAL ERROR {DOS}")
                else:
                    print(Fore.RED + f"DOSError: {DOS}")
                    print(Fore.CYAN + "Enter `help` for help")
            except Exception as e:
                print(Fore.RED + f"Found an Exception: {e}")
            except KeyboardInterrupt:
                Minecraft.DOS()
Minecraft.Config_ini()
Minecraft.Menu()
print(f"Start time at {datetime.datetime.now()}")
if not isnetconnect():
    print("not internet connect, `launch`,`help`,`clear`,`config`and`refrver` only")
if __name__ == "__main__":
    Minecraft.DOS()