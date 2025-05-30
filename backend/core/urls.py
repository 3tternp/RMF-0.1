from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import RiskViewSet, AdminDashboard, DashboardMetrics, RiskHeatmap

router = DefaultRouter()
router.register('risks', RiskViewSet, basename='risks')

urlpatterns = router.urls + [
    path('admin/dashboard/', AdminDashboard.as_view()),
    path('dashboard/metrics/', DashboardMetrics.as_view()),
    path('dashboard/heatmap/', RiskHeatmap.as_view()),
]
