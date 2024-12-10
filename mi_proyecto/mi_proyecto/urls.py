"""
URL configuration for mi_proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from mi_aplicacion import views


urlpatterns = [
    path('', views.buscar_libro, name='inicio'),
    path('crear-autor/', views.crear_autor, name='crear_autor'),
    path('crear-libro/', views.crear_libro, name='crear_libro'),
    path('crear-editorial/', views.crear_editorial, name='crear_editorial'),
]

