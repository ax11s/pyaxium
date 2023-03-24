from modules import Offsets, base
import time


def noflash():
    while True:
            player = base.pm.read_int(base.client + Offsets.dwLocalPlayer)
            if player:
                flash_value = base.player + Offsets.m_flFlashMaxAlpha
                if flash_value:
                    base.pm.write_float(flash_value, float(0))
            time.sleep(1)
noflash()