# Minecraft-DOS

`MC.py` is a Python script designed to provide a command-line interface for managing and launching Minecraft, including features for downloading and managing Minecraft versions, mods, and skins.

## Features

- Download and install various Minecraft versions (Release, Snapshot, Alpha)
- Support for mod loaders like Forge, Fabric, and Quilt
- Manage Minecraft skins (download, upload, list)
- Multi-threaded downloader for efficient file downloads
- Microsoft account login and authentication
- Manage and download mods from CurseForge and Modrinth
- System information and disk space checks

## Requirements

- Python 3.x
- Required libraries:
    - minecraft_launcher_lib
    - wget
    - keyboard
    - requests
    - colorama

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/hanhanfakedos/Minecraft-DOS.git
    ```
2. Navigate to the project directory:
    ```sh
    cd Minecraft-DOS
    ```
3. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To run the script, use the following command:
python MC.py
Commands Available in Minecraft-DOS:
listver: List all available Minecraft versions
download <version>: Download a specific Minecraft version
launch <version>: Launch a specific Minecraft version
config: Configure your profile
clear: Clear the console
refrver or F5: Refresh installed versions
mslogin: Microsoft account login
authlib: Authlib-Injector Yggdrasil Sign
alaunch <version>: Launch Minecraft with Authlib-Injector
mslaunch <version>: Launch Minecraft with Microsoft Account
modsmenu: Display available mods from CurseForge API
checkdisk: Check available disk space
sysinfo: Show system information
uninstall <version>: Uninstall a specific Minecraft version
modmenu: Fetch mods from CurseForge
downmod <ModName> <GameVersion>: Download a mod from CurseForge
modrinth: Display available mods from Modrinth API
downmodrinth <ModID> <GameVersion>: Download a mod from Modrinth
skinmanager: Manage Minecraft skins
help: Show help documentation
exit: Exit the application

## Minecraft History
Minecraft is a sandbox video game developed and published by Mojang. The game was created by Markus "Notch" Persson in the Java programming language. It was publicly released for the first time on May 17, 2009, and after gradual updates, it was fully released on November 18, 2011. Microsoft purchased Mojang and the intellectual property of Minecraft in 2014 for $2.5 billion.

## Key Milestones
2009: Minecraft's first public release
2011: Official full release of Minecraft
2014: Microsoft acquires Mojang and Minecraft
2016: Minecraft reaches 100 million registered users
2020: Minecraft becomes the best-selling video game of all time with over 200 million copies sold
Contributing
Contributions are welcome! Please fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

# Acknowledgements
Minecraft
Mojang
Code

## Example
```sh
username@host~$ python3 MC.py
Starting Minecraft-DOS....../

Initializing system components....../

Loading configurations....../

Checking network connectivity....../

Network connected


Setting up environment....../

Launching Minecraft-DOS.../

Minecraft-DOS is ready to use!


HIMEM is testing memory....../

===================================================================
                         Minecraft-DOS
===================================================================
Available Versions:
 - 1.16.5
Start time at 2025-01-12 17:08:05.775514
Enter `help` for help
{cwd}:>>>
```
## Download MCVersion
```sh
{cwd}:>>> download 1.12.2
```
next to
```
Select modloader:
fo.Forge
fa.Fabric
q.quilt
v.vanilla
0.no install
>>>
```
example forge to input:
```sh
>>>fo
```
ProgressBar
```sh
[|####################################################################################################=>|Downloaded:207/207|100%|Task:Install java runtime]
```
downloaded forge,this is example don't install OptiFine
```sh
Success Install Forge 1.12.2-14.23.5.2860
Download optifine?>>> [y|n]n
```
If you want to use authlib-injector sign in, you can
```sh
{cwd}:>>> authlib
Email:somename@example.com
Password:youpassword
```
use authlib-injector launch version
```
{cwd}:>>> alaunch 1.12.2
Spawned Launcher CMD
DOS/4GW Protected Mode Runtime Version 1.97
Copyright(c)Rational Systems, Inc. 1990-1994

Loading MineCraft 3D
(c)1991-2024 Mojang PC Repair and Software AB

Loading MINECRAFT.JAR

==============================================================================
Minecraft Log
==============================================================================

[authlib-injector] [INFO] Logging file: D:\MC\authlib-injector.log
[authlib-injector] [INFO] Version: 1.2.5
[authlib-injector] [INFO] Authentication server: https://littleskin.cn/api/yggdrasil
Enter `help` for help
```
if you want exit, you can input <exit>
```sh
{cwd}>>> exit
username@host~$
```

Feel free to customize the content based on the specific details and functionalities of your `MC.py` script.
