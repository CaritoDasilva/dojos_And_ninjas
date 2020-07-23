from django.urls import path
from . import views

urlpatterns = [
    path('add_ninja', views.add_ninja),
    path('add_dojo', views.add_dojo),
    path('', views.index)
]
