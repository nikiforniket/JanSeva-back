# -*- coding: utf-8 -*-

from common.choices import JanSevaTextChoices


class ComplaintStatusChoices(JanSevaTextChoices):
    REGISTERED = "registered", "Registered"
    IN_PROGRESS = "in_progress", "In Progress"
    REPORTED = "reported", "Reported"
    REPORT_ACKNOWLEDGED = "report_acknowledged", "Report Acknowledged"
    RESOLVED = "resolved", "Resolved"
