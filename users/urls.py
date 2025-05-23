from django.urls import path
from .views import (
    RegisterView,
    CustomTokenObtainPairView,
    LogoutView,
    UserProfileView
)

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='api-signup'),
    path('login/', CustomTokenObtainPairView.as_view(), name='api-login'),
    path('logout/', LogoutView.as_view(), name='api-logout'),
    path('profile/', UserProfileView.as_view(), name='api-profile'),
]