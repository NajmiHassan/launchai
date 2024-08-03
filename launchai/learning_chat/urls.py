from django.urls import path
from . import views

urlpatterns = [
    path('learning_chat', views.MessageAPIView.as_view(), name='learning_chat'),
]
