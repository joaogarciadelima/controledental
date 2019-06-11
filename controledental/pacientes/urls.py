from django.urls import path

from controledental.pacientes import views


app_name = 'pacientes'
urlpatterns = [
    path('', views.pacientes, name='pacientes'),
]
