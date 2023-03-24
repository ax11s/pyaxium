import keyboard
from modules import *



def bhop():
    while True:
        if keyboard.is_pressed("v"):
            force_jump = base.client + Offsets.dwForceJump
            player = base.pm.read_int(base.client + Offsets.dwLocalPlayer)
            if player:
                on_ground = base.pm.read_int(player + Offsets.m_fFlags)
                if on_ground and on_ground == 257:
                    base.pm.write_int(force_jump, 5)
                    time.sleep(0.08)
                    base.pm.write_int(force_jump, 4)

        time.sleep(0.002)


if __name__ == '__main__':
    bhop()