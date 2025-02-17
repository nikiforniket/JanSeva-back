# -*- coding: utf-8 -*-

from common.choices import JanSevaTextChoices


class ProfileTypeChoices(JanSevaTextChoices):

    ADMIN = "AD", "Admin"
    PARTY_MEMBER = "PM", "Party Member"
    VOTER = "VM", "Voter"


class ProfileTypeDocsChoices(JanSevaTextChoices):

    AADHAR = "AD", "Aadhar card"
    VOTER_CARD = "VT", "Voter card"


class GenderChoices(JanSevaTextChoices):

    MALE = "M", "Male"
    FEMALE = "F", "Female"
    OTHER = "O", "Other"