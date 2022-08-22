from django.urls import path
from . import views
from django.urls import path,include
from django.contrib import admin

urlpatterns = [
    path('', views.index),
    path('recursos/', views.recursos),
    path('beneficios/', views.beneficios),
    path('precos/', views.precos),
    path('index/', admin.site.index),
    path('admin/', admin.site.urls),

]
