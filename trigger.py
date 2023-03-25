import keyboard
from modules import *



crosshairid = base.client + Offsets.m_iCrosshairId

def trigger():
    while True:
        if keyboard.is_pressed("v") and 0 < base.pm.read_int(base.localplayer + Offsets.m_iCrosshairId):
                    base.pm.write_int(base.client + Offsets.dwForceAttack, 1)
                    time.sleep(0.5)
                    base.pm.write_int(base.client + Offsets.dwForceAttack, 0)




if __name__ == '__main__':
    trigger()