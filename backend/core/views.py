from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Risk, User
from .serializers import RiskSerializer
from .permissions import IsAdmin, IsManager, ReadOnlyOrAdminManager
from django.db.models import Count

class RiskViewSet(ModelViewSet):
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer
    permission_classes = [IsAuthenticated, ReadOnlyOrAdminManager]

class AdminDashboard(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    def get(self, request):
        return Response({"message": "Welcome Admin"})

class DashboardMetrics(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({
            "total_risks": Risk.objects.count(),
            "by_severity": Risk.objects.values("severity").annotate(count=Count("id")),
            "top_owners": Risk.objects.values("owner__username").annotate(count=Count("id")).order_by("-count")[:5]
        })

class RiskHeatmap(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        matrix = [[0 for _ in range(5)] for _ in range(4)]  # Likelihood 1–4, Severity 1–5
        for r in Risk.objects.all():
            matrix[r.likelihood - 1][r.severity - 1] += 1
        return Response({"heatmap": matrix})
