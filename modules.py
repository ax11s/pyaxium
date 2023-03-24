import pymem
import pymem.process
import sys
from requests import get



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


class Offsets:
   
    pass
getoffsets()

class base():
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    pass

