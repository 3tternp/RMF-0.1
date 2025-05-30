from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Framework, Control
from .serializers import FrameworkSerializer, ControlSerializer
from core.permissions import IsAdmin, ReadOnlyOrAdminManager

class FrameworkViewSet(viewsets.ModelViewSet):
    queryset = Framework.objects.all()
    serializer_class = FrameworkSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class ControlViewSet(viewsets.ModelViewSet):
    queryset = Control.objects.select_related('framework', 'owner').prefetch_related('risks').all()
    serializer_class = ControlSerializer
    permission_classes = [IsAuthenticated, ReadOnlyOrAdminManager]
