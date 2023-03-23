import sys
from requests import get
from pymem import *
from pymem.process import *


class Offsets:
    pass

try:
        haze = get(
            "https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json"
        ).json()

        [setattr(Offsets, k, v) for k, v in haze["signatures"].items()]
        [setattr(Offsets, k, v) for k, v in haze["netvars"].items()]
except:
        sys.exit("Unable to fetch Hazedumper's Offsets")



game_proc = pymem.Pymem("csgo.exe")
game_module = module_from_name(game_proc.process_handle, "client.dll").lpBaseOfDll

local_player = pymem.read_int()

