from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import signup, signin

urlpatterns = [
    path('', signup, name="app_siginup"),
    path('/signin/', signin, name="app_signin"),
    path('/signup/', signup, name="app_signup"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
