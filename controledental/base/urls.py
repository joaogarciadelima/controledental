from django.urls import path

from controledental.base.views import home


app_name = 'base'
urlpatterns = [
    path('home', home, name='home'),
]
