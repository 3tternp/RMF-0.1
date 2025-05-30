from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdmin
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Risk
from .serializers import RiskSerializer
from django.db.models import Count
from datetime import timedelta
from django.utils import timezone
from .permissions import ReadOnlyOrAdminManager

class AdminDashboard(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    def get(self, request):
        return Response({"message": "Welcome Admin"})

class RiskViewSet(viewsets.ModelViewSet):
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer
    permission_classes = [IsAuthenticated, ReadOnlyOrAdminManager]

class DashboardMetrics(APIView):
    permission_classes = [IsAuthenticated, ReadOnlyOrAdminManager]

    def get(self, request):
        now = timezone.now()
        last_30_days = now - timedelta(days=30)

        total_risks = Risk.objects.count()
        by_status = Risk.objects.values('status').annotate(count=Count('id'))
        by_severity = Risk.objects.values('severity').annotate(count=Count('id'))
        recent_risks = Risk.objects.filter(created_at__gte=last_30_days).count()
        top_owners = Risk.objects.values('owner__username').annotate(count=Count('id')).order_by('-count')[:5]

        return Response({
            "total_risks": total_risks,
            "risks_by_status": by_status,
            "risks_by_severity": by_severity,
            "recent_risks_30d": recent_risks,
            "top_risk_owners": top_owners,
        })
