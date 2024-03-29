from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name = "home"),
    path('about/', views.about, name = "about"),
    path('gallery/', views.gallery, name = "gallery"),
    path('contact/', views.contact, name = "contact"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)