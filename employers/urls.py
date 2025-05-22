from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from accounts.views import RegisterView, LogoutView, ProfileView
from employers.views import EmployerListCreateView, EmployerDetailView

urlpatterns = [
    # ... other paths ...
    # JWT login and token refresh
    path('api/auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Registration (signup)
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    # Logout (blacklist refresh token)
    path('api/auth/logout/', LogoutView.as_view(), name='logout'),
    # User profile (retrieve/update own user)
    path('api/auth/profile/', ProfileView.as_view(), name='profile'),

    # Employer CRUD (see below)
    path('api/employers/', EmployerListCreateView.as_view(), name='employer-list'),
    path('api/employers/<int:pk>/', EmployerDetailView.as_view(), name='employer-detail'),
]
