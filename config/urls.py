"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include
from django.conf import settings # For media files
from django.conf.urls.static import static # For media files


# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
#     # path('accounts', include('accounts.urls')),
#     path('users', include('users.urls')),
#     path('employers', include('employers.urls')),


# ]

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views
from employers import views as employer_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API URLs
    path('api/auth/', include('users.urls')),
    path('api/employers/', include('employers.urls')),
    path('news/', include('news.urls')),
    
    # Template URLs
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', user_views.SignUpView.as_view(), name='signup'),
    path('profile/', user_views.ProfileView.as_view(), name='profile'),
    
    path('employers/', employer_views.EmployerListView.as_view(), name='employer-list'),
    path('employers/create/', employer_views.EmployerCreateView.as_view(), name='employer-create'),
    path('employers/<int:pk>/', employer_views.EmployerDetailView.as_view(), name='employer-detail'),
    path('employers/<int:pk>/update/', employer_views.EmployerUpdateView.as_view(), name='employer-update'),
    path('employers/<int:pk>/delete/', employer_views.EmployerDeleteView.as_view(), name='employer-delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   # For media files