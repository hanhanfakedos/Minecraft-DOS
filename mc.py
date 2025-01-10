#-*- coding:utf-8 -*-
import os
import subprocess
import uuid
import sys
import time
import configparser
import platform
import socket
import tempfile
import base64
import webbrowser
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
except ModuleNotFoundError:
    pipdown("minecraft_launcher_lib")
    pipdown("wget")
    pipdown("keyboard")
    pipdown("requests")

if platform.architecture()[0] == '32bit':
    print("Sorry,The system is unsupport this version")
    exit()

__author__="HomingThistle3770"
cwd = os.getcwd()
try:
    os.makedirs(rf"{cwd}/.minecraft")
    os.makedirs(rf"{cwd}/.minecraft/assets")
    os.makedirs(rf"{cwd}/.minecraft/libraries/moe/yushi/authlib-injector")
    os.makedirs(rf"{cwd}/.minecraft/versions")
except FileExistsError:
    pass

tempfolder=tempfile.mkdtemp("Minecraft-DOS")

start=time.perf_counter()
defaultMinecraftDir=rf"{cwd}/.minecraft"
conf = configparser.ConfigParser()
clientid="5c4883c1-e9c3-4469-80e3-35c9e0238103"
redirecturi="https://login.microsoftonline.com/common/oauth2/nativeclient"
authlibjson=requests.get("https://authlib-injector.yushi.moe/artifact/latest.json").json()
authlibURL=authlibjson["download_url"]
authver=authlibjson["version"]
authlibPath=f"{cwd}/.minecraft/libraries/moe/yushi/authlib-injector/authlib-injector-{authver}.jar"
if not os.path.exists(authlibPath):
    wget.download(authlibURL,authlibPath)
MSloginData={}
YggdrasilURL="https://littleskin.cn/api/yggdrasil"
AuthlibB64=str(base64.b64encode(str(requests.get(YggdrasilURL).json()).encode('utf-8')),'utf-8')

def isnetconnect():
    ipaddress = socket.gethostbyname(socket.gethostname())
    if ipaddress == '127.0.0.1':
        return False
    else:
        return True
class Minecraft:
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
        if os.path.exists("config.ini") != True:
            with open("config.ini","w") as confFile:
                conf.write(confFile)
            conf.read("config.ini")
        else:
            conf.read("config.ini")

    def ask_yes_no(text: str) -> bool:
        while True:
            answer = input(text + " [y|n]")
            if answer.lower() == "y":
                return True
            elif answer.lower() == "n":
                return False
            else:
                print("Please enter y or n")
    def Menu():
        print(f"""===================================================================
Minecraft-DOS
===================================================================
There version is available:{minecraft_launcher_lib.utils.get_installed_versions(defaultMinecraftDir)}""")
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

        if types == "release":
            for z in VERSIONRel:
                print(f"""\nThere Minecraft version is ready:\n----------------------------------------------------\nreleases:\n{z}\n----------------------------------------------------""")
        elif types == "snapshot":
            for s in VERSIONSna:print(f"""\nThere Minecraft version is ready:\n----------------------------------------------------\nreleases:\n{s}\n----------------------------------------------------""")
        else:
            for s0 in VERSIONBeta:print(f"""\nThere Minecraft version is ready:\n----------------------------------------------------\nreleases:\n{s0}\n----------------------------------------------------""")
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
                print(f"|{finish}=>{notfinish}|Downloaded:{progress}/{current_max}---{int(progress/current_max*100)}%---Used:{round(time.perf_counter()-start,2)}---Task:{statusII}---", end="")
                sys.stdout.flush()

        def set_max(new_max: int):
            global current_max
            current_max = new_max

        def optifine(ver):
            """Forge+Optifine==Best group"""
            optifineURL=requests.get(f"https://bmclapi2.bangbang93.com/optifine/{ver}").json()
            f3=[]
            if not optifineURL:
                print("unavaliable")
            for i in optifineURL:
                if not 'pre' in i['patch']:
                    f3.append("OptiFine_{}_{}_{}.jar".format(i['mcversion'],i['type'],i['patch']))
            print("Avaliable version:{}".format(f3))
            if not os.path.exists(f"{defaultMinecraftDir}/versions/{ver}/mods"):
                os.makedirs(f"{defaultMinecraftDir}/versions/{ver}/mods")
            while True:
                b=input("Select version(if not to exit)")
                if b in f3:
                    if not os.path.exists(f"{tempfolder}/optifine.jar"):
                        wget.download(f"https://bmclapi2.bangbang93.com/maven/com/optifine/{ver}/{b}",f"{defaultMinecraftDir}/versions/{ver}/mods/optifine.jar")
                        break
                else:
                    if not os.path.exists(f"{tempfolder}/optifine.jar"):
                        wget.download(f"https://bmclapi2.bangbang93.com/maven/com/optifine/{ver}/{f3[-1]}",f"{defaultMinecraftDir}/versions/{ver}/mods/optifine.jar")
                        break

        def fabricAPI(ver):
            """Fabric mods need Fabric API"""
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
                        if not os.path.exists(f"{defaultMinecraftDir}/versions/{ver}/mods/{c2[xc]}"):
                            wget.download(c1[xc],f"{defaultMinecraftDir}/versions/{ver}/mods/{c2[xc]}")
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

        def Download(ver):
            """TODo..."""
            callback={"setStatus":Minecraft.installMinecraft.set_status,"setProgress":Minecraft.installMinecraft.set_progress,"setMax":Minecraft.installMinecraft.set_max}
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

    class RunMinecraft(Thread):
        """Use Minecraft.RunMinecraft.Run(U Version,Username,UUID,Token,Memory) to run"""
        def Run(ver, username, uuid, token, Xmx:int, authlib=False):
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
                options["jvmArguments"] = ["-client",f"-Xmx{Xmx}m",f"-Xms{Xmx}m","-Xss1m","-XX:-UseAdaptiveSizePolicy","-XX:+UseG1GC","-XX:-UseAdaptiveSizePolicy","-XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump"]
                if authlib:
                    options["jvmArguments"].append(f"-javaagent:{authlibPath}={YggdrasilURL}")
                    options["-Dauthlibinjector.side"]='client'
                    options["-Dauthlibinjector.yggdrasil.prefetched"]=AuthlibB64
                minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(ver, defaultMinecraftDir , options)
                print("Spawned Launcher CMD")
                print(f"Run Minecraft With {minecraft_command}")
                print("""DOS/4GW Protected Mode Runtime Version 1.97\nCopyright(c)Rational Systems, Inc. 1990-1994\n\nLoading MineCraft 3D\n(c)1991-2024 Mojang PC Repair and Software AB\n\nLoading MINECRAFT.JAR""")
                print("""
==============================================================================
Minecraft Log
==============================================================================
""")
                x2=open("Logs.log","a")
                x2.write(subprocess.call(minecraft_command))
                print("EXIT")
            except minecraft_launcher_lib.exceptions.VersionNotFound:
                if Minecraft.ask_yes_no("Do you want install the version") == True:
                    Minecraft.installMinecraft.Download(ver)
            except Exception as e:
                print("ERROR!",e)
    def ConfPanel():
        conf.read("config.ini")
        print("""CONFIG PANEL\nYou can change username and Mems\n(1)Change Name\n(2)Change XMX\n(3)Change AuthURL\n(4)Exit""")
        while True:
            choose=input("Choose a selections >")
            if choose == "1":
                c=input("Write a new name(Enter exit0 to exit) >>>")
                if c != "exit0":
                    conf["user"]["Username"] = c
                else:
                    pass
            elif choose == "2":
                try:
                    mem=input("Set Memory(Enter 0 to exit) >>>")
                    if mem != "0" :
                        conf["JVMMemory"]["Xmx"] = mem
                    else:
                        pass
                except ValueError:
                    print("Not a valid number")
            elif choose == "3":
                try:
                    url=input("Choose URL")
                    urllib.request.urlopen(url)
                    global YggdrasilURL
                    YggdrasilURL=url
                except ValueError:
                    print("FakeURL")
                except Exception as e:
                    print("Error:",e)
                
            elif choose == "4":
                break
            with open("config.ini", "w") as configfile:
                conf.write(configfile)
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
            conf.read("config.ini")
            conf["userAuthlib"]["Username"] = requestJson["selectedProfile"]["name"]
            conf["userAuthlib"]["UUID"]=requestJson["selectedProfile"]["id"]
            conf["userAuthlib"]["Token"]=requestJson["accessToken"]
            with open("config.ini", "w") as configfile:
                conf.write(configfile)
        else:
            print("ERROR:",requestJson["errorMessage"])
    def DOS():
        conf = configparser.ConfigParser()
        conf.read("config.ini")
        username1=conf["user"]["Username"]
        uuid1=conf["user"]["UUID"]
        token1=conf["user"]["Token"]
        Xmx1=conf["JVMMemory"]["Xmx"]
        helpf="""
Minecraft-DOS Help documents
----------------------------------------------------
listver (None)
List all version
----------------------------------------------------
download (Vers)
Download a version
----------------------------------------------------
launch (Vers)
Launch a version
----------------------------------------------------
config (None)
Configure you profile
----------------------------------------------------
clear (None)
Clear Console
----------------------------------------------------
refrver or F5 (None)
Refresh installed versions
----------------------------------------------------
mslogin (None)
Microsoft Login
----------------------------------------------------
authlib (None)
Authlib-Injector Yggdrasil Sign
----------------------------------------------------
alaunch (Vers)
Authlib-Injector Launch
----------------------------------------------------
mslaunch (Vers)
Microsoft Account Launch
----------------------------------------------------
"""
        print("Enter `help` to help")
        while True:
            try:
                DOS=input("MC-DOS's Shell >>>")
                if 'download ' in DOS.lower() and DOS.index("d") == 0:
                    c=DOS.lower()
                    Vers=c.replace("download ", '')
                    Minecraft.installMinecraft.Download(Vers)
                elif 'launch ' in DOS and DOS.index("l") == 0:
                    c=DOS.lower()
                    Vers2=c.replace("launch ", '')
                    Minecraft.RunMinecraft.Run(Vers2,username1,uuid1,token1,Xmx1)
                elif DOS == "config":
                    Minecraft.ConfPanel()
                elif DOS == "listver":
                    print("""List versions\nTypes:\n(1)Release\n(2)Snapshot\n(3)Old Alpha\n(4)Exit\n(Can Multi choose)""")
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
                elif DOS == "mslogin":
                    Minecraft.MSLogin()
                    conf = configparser.ConfigParser()
                    conf.read("config.ini")
                    conf["userMS"]["Username"] = MSloginData["name"]
                    conf["userMS"]["UUID"]=MSloginData["id"]
                    conf["userMS"]["Token"]=MSloginData["access_token"]
                    with open("config.ini", "w") as configfile:
                        conf.write(configfile)
                elif 'mslaunch ' in DOS and DOS.index("a") == 0:
                    c=DOS.lower()
                    Vers21=c.replace("alaunch ", '')
                    conf = configparser.ConfigParser()
                    conf.read("config.ini")
                    Minecraft.RunMinecraft.Run(Vers21,conf["userMS"]["Username"],conf["userMS"]["UUID"],conf["userMS"]["Token"],Xmx1,authlib=True)
                elif DOS == "authlib":
                    email=input("Email:")
                    passwd=input("Password:")
                    Minecraft.AuthlibSign(YggdrasilURL,email,passwd)
                elif 'alaunch ' in DOS and DOS.index("a") == 0:
                    c=DOS.lower()
                    Vers21=c.replace("alaunch ", '')
                    conf = configparser.ConfigParser()
                    conf.read("config.ini")
                    Minecraft.RunMinecraft.Run(Vers21,conf["userAuthlib"]["Username"],conf["userAuthlib"]["UUID"],conf["userAuthlib"]["Token"],Xmx1,authlib=True)
                elif DOS == "help":
                    print(helpf)
                elif DOS == "clear":
                    print("\033c",end="")
                elif DOS == "refrver" or keyboard.is_pressed("f5"):
                    minecraft_launcher_lib.utils.get_installed_versions(defaultMinecraftDir)
                    time.sleep(0.5)
                elif DOS == '':
                    pass
                elif DOS == 'exit':
                    sys.exit(0)
                else:
                    print("DOSError:{}".format(DOS))
                    print("Enter `help` to help")
            except Exception as e:
                print("Found a Exception:{}".format(e))
            except KeyboardInterrupt:
                Minecraft.DOS()
    def DOSfile(online=False):
        DOSCode=r"""import os
import datetime
import mc
import sys
import time

mc.Minecraft.OOO("Starting Minecraft-DOS",15,0.1)

if sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")
Minecraft.Menu()
print(f"Start time at {datetime.datetime.now()}")
if not mc.isnetconnect():
    print("not internet connect, `launch`,`help`,`clear`,`config`and`refrver` only")
Minecraft.DOS()
        """
        if online:
            exec(DOSCode)
        else:
            DOSFile=open("DOS.py","w")
            DOSFile.write(DOSCode)

Minecraft.Config_ini()
if Minecraft.ask_yes_no("Online mode is Yes"):
    Minecraft.DOSfile(online=True)
else:
    Minecraft.DOSfile()
