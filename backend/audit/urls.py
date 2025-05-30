from rest_framework.routers import DefaultRouter
from .views import AuditViewSet, IncidentViewSet

router = DefaultRouter()
router.register('audits', AuditViewSet, basename='audits')
router.register('incidents', IncidentViewSet, basename='incidents')

urlpatterns = router.urls
