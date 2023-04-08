import keyboard
from modules import *





def trigger():
    crosshairid = base.client + Offsets.m_iCrosshairId
    while True:
        time.sleep(0.001)
        if keyboard.is_pressed("c") and 0 < base.pm.read_int(base.localplayer + Offsets.m_iCrosshairId):
                    base.pm.write_int(base.client + Offsets.dwForceAttack, 1)
                    time.sleep(0.01)
                    base.pm.write_int(base.client + Offsets.dwForceAttack, 0)




if __name__ == '__main__':
    trigger()