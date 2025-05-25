from django.urls import path
from .views import news

# for media file
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('news', news, name='news')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
