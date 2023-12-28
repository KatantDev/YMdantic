import sys

if sys.version_info >= (3, 11):
    from enum import StrEnum
else:
    from strenum import StrEnum


class OpenPlaylistEnum(StrEnum):
    RUSSIA_SUPERLAUNCH = "open-playlist/RUSSIA_superlaunch"
    PEREMOTKA = "peremotka/smart-open-playlist/REWIND_2023"
    RU_TOP100OF2023 = "open-playlist/RU_top100of2023"
