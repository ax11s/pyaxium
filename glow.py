from modules import *



def main():

    while True:
        glow_manager = base.pm.read_int(base.client + Offsets.dwGlowObjectManager)

        for i in range(1, 32):  # Entities 1-32 are reserved for players.
            entity = base.pm.read_int(base.client + Offsets.dwEntityList + i * 0x10)

            if entity:
                entity_team_id = base.pm.read_int(entity + Offsets.m_iTeamNum)
                entity_glow = base.pm.read_int(entity + Offsets.m_iGlowIndex)

                if entity_team_id == 2:  # Terrorist
                    base.pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(1))   # R
                    base.pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))   # G
                    base.pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))   # B
                    base.pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1))  # Alpha
                    base.pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)           # Enable glow

                elif entity_team_id == 3:  # Counter-terrorist
                    base.pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(0))   # R
                    base.pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))   # G
                    base.pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(1))   # B
                    base.pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1))  # Alpha
                    base.pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)           # Enable glow


if __name__ == '__main__':
    main()