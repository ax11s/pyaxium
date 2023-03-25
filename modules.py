import pymem
import pymem.process
import sys
from requests import get
import time



class Offsets:
    pass


def getoffsets():
    try:
        haze = get(
            "https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json"
        ).json()

        [setattr(Offsets, k, v) for k, v in haze["signatures"].items()]
        [setattr(Offsets, k, v) for k, v in haze["netvars"].items()]
        print("offsets fetched succesfuly")
    except:
        sys.exit("Unable to fetch Hazedumper's Offsets")


getoffsets()

class base():
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    localplayer = pm.read_int(client + Offsets.dwLocalPlayer)
    pass

