import keyboard
from modules import *



def bunny():
    while True:
        if keyboard.is_pressed("v"):
            force_jump = base.client + Offsets.dwForceJump

            if base.localplayer:
                on_ground = base.pm.read_int(base.localplayer + Offsets.m_fFlags)
                if on_ground and on_ground == 257:
                    base.pm.write_int(force_jump, 5)
                    time.sleep(0.08)
                    base.pm.write_int(force_jump, 4)

        time.sleep(0.002)


if __name__ == '__main__':
    bunny()