from django.urls import path

from controledental.tratamento import views


app_name = 'tratamento'
urlpatterns = [
    path('', views.tratamentos, name='tratamento'),
]
