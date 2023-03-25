import keyboard
from modules import *



crosshairid = base.client + Offsets.m_iCrosshairId

def trigger():
    while True:
        if keyboard.is_pressed("v"):
                crosshair = base.pm.read_int(base.localplayer, Offsets.m_iCrosshairId)
                print(crosshair)




if __name__ == '__main__':
    trigger()