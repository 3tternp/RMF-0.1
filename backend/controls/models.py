from django.db import models
from django.conf import settings

class Framework(models.Model):
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} {self.version or ''}".strip()

class Control(models.Model):
    framework = models.ForeignKey(Framework, on_delete=models.CASCADE, related_name='controls')
    control_id = models.CharField(max_length=50)  # e.g., AC-1
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100, blank=True)
    family = models.CharField(max_length=100, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.control_id} - {self.title}"

