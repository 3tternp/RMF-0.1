from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Audit, Incident
from .serializers import AuditSerializer, IncidentSerializer
from core.permissions import IsAdmin, ReadOnlyOrAdminManager

class AuditViewSet(viewsets.ModelViewSet):
    queryset = Audit.objects.prefetch_related('risks', 'controls').all()
    serializer_class = AuditSerializer
    permission_classes = [IsAuthenticated, ReadOnlyOrAdminManager]

class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.select_related('audit', 'reported_by').all()
    serializer_class = IncidentSerializer
    permission_classes = [IsAuthenticated, ReadOnlyOrAdminManager]
