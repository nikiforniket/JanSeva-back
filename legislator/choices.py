# -*- coding: utf-8 -*-

from common.choices import JanSevaTextChoices


class RepresentativeTypeChoices(JanSevaTextChoices):
    MP = "MP", "Member of Parliament"
    MLA = "MLA", "Member of Legislative Assembly"
    SARPANCH = "SARPANCH", "Sarpanch"
    UP_SARPANCH = "UP_SARPANCH", "Up-Sarpanch"
    MEMBER = "MEMBER", "Member"
    CHAIRMAN = "CHAIRMAN