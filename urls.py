"""
URL configuration for djtrain01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from apptrain01 import views

urlpatterns = [
    path('', views.index),
    path('index.html', views.index),
    path('info.html', views.info),
    path('kolonka_info.html', views.testform),
    path('zapravka.html', views.zapravka),
    path('zapravka_info.html', views.zapravka_info),
    path('popolnenie.html', views.popolnenie),
    path('popolnenie_info.html', views.popolnenie_info),
    path('popolnenie_prom.html', views.popolnenie_prom),
    path('popolnenie_prom_info.html', views.popolnenie_prom_info),
    path('korrektirovka.html', views.korrektirovka),
    path('korrektirovka_info.html', views.korrektirovka_info),
    path('korrektirovka_prom.html', views.korrektirovka_prom),
    path('korrektirovka_prom_info.html', views.korrektirovka_prom_info),
]

