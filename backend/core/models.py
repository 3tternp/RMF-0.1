from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

class Role(models.TextChoices):
    ADMIN = 'admin', 'Admin'
    MANAGER = 'manager', 'Manager'
    AUDITOR = 'auditor', 'Auditor'
    VIEWER = 'viewer', 'Viewer'

class User(AbstractUser):
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.VIEWER)

class Risk(models.Model):
    SEVERITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ]

    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    likelihood = models.PositiveSmallIntegerField(help_text="Scale: 1 (low) to 5 (high)")
    mitigation_plan = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
