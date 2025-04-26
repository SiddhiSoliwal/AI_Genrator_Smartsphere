
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Chatpage, name='chatpage'),  # Ensure the case matches the folder name
]