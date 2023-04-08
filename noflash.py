from modules import *


def noflash():
    while True:
            if base.localplayer:
                flash_value = base.localplayer + Offsets.m_flFlashMaxAlpha
                if flash_value:
                    base.pm.write_float(flash_value, float(0))
            time.sleep(0.1)

if __name__ == '__main__': 
    noflash()