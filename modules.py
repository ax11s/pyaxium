import sys
from requests import get
import psutil
import ctypes
import numpy as np


processes = psutil.process_iter()

for process in processes:
    if process.name() == "csgo.exe":
          my_process = psutil.Process(process.pid)
          


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

