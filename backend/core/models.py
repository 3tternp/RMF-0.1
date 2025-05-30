from django.contrib.auth.models import AbstractUser
from django.db import models

class Role(models.TextChoices):
    ADMIN = 'admin', 'Admin'
    MANAGER = 'manager', 'Manager'
    AUDITOR = 'auditor', 'Auditor'
    VIEWER = 'viewer', 'Viewer'

class User(AbstractUser):
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.VIEWER)
