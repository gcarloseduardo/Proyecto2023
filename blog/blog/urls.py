"""
URL configuration for blog project.

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
from django.urls import path, include # Importamos include, para poder trabajar con las urls de noticias
from apps.noticias import views
from . import views

# URL PRINCIPAL

urlpatterns = [
    path('admin/', admin.site.urls),
    # path para la url de la vista de home
    path('', views.home, name = 'home'),
    # path tiene 3 parametros, la dirección url, la funcion de la vista(views), y name
    path('nosotros/', views.nosotros, name = 'nosotros'),
    #................URL APP NOTICIA...................
    path('noticias/', include('apps.noticias.urls')),
]
