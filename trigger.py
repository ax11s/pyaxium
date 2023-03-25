import keyboard
from modules import *




def trigger():
    while True:
        if keyboard.is_pressed("v"):
                base.pm.write_int(base.client + Offsets.dwForceAttack, 1)
                time.sleep(0.1)
                base.pm.write_int(base.client + Offsets.dwForceAttack, 0)



if __name__ == '__main__':
    trigger()