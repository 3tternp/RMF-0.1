from django.db import models
from django.conf import settings
from core.models import Risk
from controls.models import Control

class Audit(models.Model):
    AUDIT_STATUS_CHOICES = [
        ('planned', 'Planned'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('closed', 'Closed'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=AUDIT_STATUS_CHOICES, default='planned')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='created_audits')
    risks = models.ManyToManyField(Risk, blank=True, related_name='audits')
    controls = models.ManyToManyField(Control, blank=True, related_name='audits')

    def __str__(self):
        return self.title

class Incident(models.Model):
    INCIDENT_SEVERITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ]

    audit = models.ForeignKey(Audit, on_delete=models.CASCADE, related_name='incidents')
    title = models.CharField(max_length=255)
    description = models.TextField()
    reported_at = models.DateTimeField(auto_now_add=True)
    severity = models.CharField(max_length=10, choices=INCIDENT_SEVERITY_CHOICES, default='low')
    reported_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='reported_incidents')
    resolved = models.BooleanField(default=False)
    resolution_notes = models.TextField(blank=True, null=True)
    resolved_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
