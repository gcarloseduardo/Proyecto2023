from django.urls import path
from . import views

app_name = "noticias"

# urls de app noticias
urlpatterns = [
    path("", views.inicio, name= "inicio"),


]