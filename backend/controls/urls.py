from rest_framework.routers import DefaultRouter
from .views import FrameworkViewSet, ControlViewSet

router = DefaultRouter()
router.register('frameworks', FrameworkViewSet, basename='frameworks')
router.register('controls', ControlViewSet, basename='controls')

urlpatterns = router.urls

