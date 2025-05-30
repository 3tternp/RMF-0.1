from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdmin
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Risk
from .serializers import RiskSerializer
from .permissions import ReadOnlyOrAdminManager

class AdminDashboard(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    def get(self, request):
        return Response({"message": "Welcome Admin"})

class RiskViewSet(viewsets.ModelViewSet):
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer
    permission_classes = [IsAuthenticated, ReadOnlyOrAdminManager]
