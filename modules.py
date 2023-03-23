import sys
from requests import get
import pymem
import pymem.process

pymem.get_process_name("csgo.exe")


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


