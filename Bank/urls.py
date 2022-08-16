from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('api/',include("api.urls")),
    path("", include("apps.authentication.urls")), 
    path("", include("apps.home.urls")),
    path('api_auth/', include('rest_framework.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)