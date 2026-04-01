from django.urls import path
from . import views

urlpatterns = [
    path('echavez_app', views.echavez_app, name='echavez_app'),
]