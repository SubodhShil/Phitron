from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('firstapp/', include("firstapp.urls")),
    path('contact/', views.contact),
    path('home/', views.home),
]
