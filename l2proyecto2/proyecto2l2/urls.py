from django.urls import path
from . import views

urlpatterns = [
    path('template1/', views.template1, name='template1'),
    path('template2/', views.template2, name='template2'),
]
