from django.urls import path
from . import views

urlpatterns = [
    path('', views.Contactpage, name='Contactpage'),  # Ensure the case matches the folder name
]