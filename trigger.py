import keyboard
from modules import *




def trigger():
    while True:


        if keyboard.is_pressed("c"):
            player = base.pm.read_int(base.client + Offsets.dwLocalPlayer)
            entity_id = base.pm.read_int(base.player + Offsets.m_iCrosshairId)
            entity = base.pm.read_int(base.client + Offsets.dwEntityList + (entity_id - 1) * 0x10)

            entity_team = base.pm.read_int(entity + Offsets.m_iTeamNum)
            player_team = base.pm.read_int(player + Offsets.m_iTeamNum)

            if entity_id > 0 and entity_id <= 64 and player_team != entity_team:
                base.pm.write_int(base.client + Offsets.dwForceAttack, 6)

            time.sleep(0.006)


if __name__ == '__main__':
    trigger()