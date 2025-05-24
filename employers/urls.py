from django.urls import path
from .views import EmployerListCreateView, EmployerDetailView

urlpatterns = [
    path('', EmployerListCreateView.as_view(), name='api-employer-list'),
    path('<int:id>/', EmployerDetailView.as_view(), name='api-employer-detail'),
]