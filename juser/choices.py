# -*- coding: utf-8 -*-

from common.choices import JanSevaTextChoices


class ProfileTypeChoices(JanSevaTextChoices):

    ADMIN = "AD", "Admin"
    PARTY_MEMBER = "PM", "Party Member"


class ProfileTypeDocsChoices(JanSevaTextChoices):

    AADHAR = "AD", "Aadhar card"
    VOTER_CARD = "VT", "Voter card"