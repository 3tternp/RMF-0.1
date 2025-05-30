from django.urls import path
from .views import AdminDashboard

urlpatterns = [
    path('admin/dashboard/', AdminDashboard.as_view()),
]
