from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path("", home),
]

urlpatterns = [
    path("", views.lista_funcionarios, name="lista_funcionarios"),
]