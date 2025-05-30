
from django.urls import path
from .views import AdminDashboard
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RiskViewSet, AdminDashboard

router = DefaultRouter()
router.register(r'risks', RiskViewSet)

urlpatterns = [
    path('admin/dashboard/', AdminDashboard.as_view()),
    path('', include(router.urls)),
]
