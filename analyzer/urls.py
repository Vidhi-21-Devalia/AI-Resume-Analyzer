from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_resume, name='upload_resume'),
    path('result/<int:pk>/', views.result, name='result'),
]
