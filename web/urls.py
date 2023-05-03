from django.urls import path

from . import views

app_name = 'web'

urlpatterns = [
    path('', views.AlumnoView.as_view(),name='index'),
    path('listProfesor/', views.ProfesorView.as_view(),name='listProfesor')
]