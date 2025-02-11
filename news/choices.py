# -*- coding: utf-8 -*-

from django.db import models

class NewStatusChoices(models.TextChoices):

    CREATED = "created", "Created"
    IN_APPROVAL = "in_approval", "In approval"
    APPROVED = "approved", "Approved"
    ACTIVE = "active", "Active"
    INACTIVE = "inactive", "In active"
