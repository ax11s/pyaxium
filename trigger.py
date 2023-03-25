import keyboard
from modules import *




def trigger():
    while(base.pm.r_int(base.proc, base.localplayer + Offsets.m_fFlags) == 257) and base.pm.key_pressed(86):
                base.pm.w_int(base.pm , base.client + Offsets.dwForceAttack, 1)
                time.sleep(0.1)
                base.pm.w_int(base.pm , base.client + Offsets.dwForceAttack, 0)



if __name__ == '__main__':
    trigger()