from django.urls import path
from . import views

urlpatterns = [
    path('bstest', views.bstest, name='bstest'),
    path('', views.index, name='index'),
]
