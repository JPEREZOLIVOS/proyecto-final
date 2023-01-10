"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from ejemplo.views import index, saludar_a, sumar, buscar
from Finanzas_Personales.views import (index, PostDetalle, PostListar, PostCrear, PostBorrar, PostActualizar, UserSignUp, UserLogin, UserLogout, AvatarActualizar, UserActualizar, MensajeCrear, MensajeListar, MensajeDetalle, MensajeBorrar)
from django.contrib.admin.views.decorators import staff_member_required


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/',index),
    path('saludar-a/<nombre>/',saludar_a),
    path('sumar/<int:a>/<int:b>/', sumar),
    path('buscar/',buscar),
    path('Finanzas-Personales/', index, name='Finanzas-Personales-index'),
    path('Finanzas-Personales/<int:pk>/detalle/', PostDetalle.as_view(), name="Finanzas-Personales-detalle"),
    path('Finanzas-Personales/listar/', PostListar.as_view(), name="Finanzas-Personales-listar"),
    path('Finanzas-Personales/crear/', staff_member_required(PostCrear.as_view()), name='Finanzas-Personales-crear'),
    path('Finanzas-Personales/<int:pk>/borrar/', staff_member_required(PostBorrar.as_view()), name="Finanzas-Personales-borrar"),
    path('Finanzas-Personales/<int:pk>/actualizar/', staff_member_required(PostActualizar.as_view()), name="Finanzas-Personales-actualizar"),
    path('Finanzas-Personales/signup/',UserSignUp.as_view(), name='Finanzas-Personales-signup'),
    path('Finanzas-Personales/login/',UserLogin.as_view(), name='Finanzas-Personales-login'),
    path('Finanzas-Personales/logout/',UserLogout.as_view(), name='Finanzas-Personales-logout'),
    path('Finanzas-Personales/avatares/<int:pk>/actualizar/',AvatarActualizar.as_view(), name='Finanzas-Personales-avatar-actualizar'),
    path('Finanzas-Personales/users/<int:pk>/actualizar/', UserActualizar.as_view(), name='Finanzas-Personales-users-actualizar'),
    path('Finanzas-Personales/mensajes/crear/', MensajeCrear.as_view(), name='Finanzas-Personales-mensajes-crear'),
    path('Finanzas-Personales/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name='Finanzas-Personales-mensajes-detalle'),
    path('Finanzas-Personales/mensajes/listar/', MensajeListar.as_view(), name='Finanzas-Personales-mensajes-listar'),
    path('Finanzas-Personales/mensajes/<int:pk>/detalle/', MensajeBorrar.as_view(), name='Finanzas-Personales-mensajes-borrar'),
    path('Finanzas-Personales/about', TemplateView.as_view(template_name='Finanzas_Personales/about.html'), name='Finanzas-Personales-about'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)