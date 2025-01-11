# -*- coding: utf-8 -*-

from common.choices import JanSevaTextChoices


class ComplaintStatusChoices(JanSevaTextChoices):
    REGISTERED = "registered", "Registered"
    IN_PROGRESS = "in_progress", "In Progress"
    REPORTED = "reported", "Reported"
    REPORT_ACKNOWLEDGED = "report_acknowledged", "Report Acknowledged"
    RESOLVED = "resolved", "Resolved"


class GeoLocationComplaintChoices(JanSevaTextChoices):
    POOT_HOLE = "poot_hole", "Poot Hole"
    STREET_LIGHT = "street_light", "Street Light"
    GARBAGE = "garbage", "Garbage"
    DRAINAGE = "drainage", "Drainage"
    PIPE_LEAK = "pipe_leak", "Pipe Leak"