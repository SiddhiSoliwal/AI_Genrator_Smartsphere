from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('About/', views.About, name='About'),
    path('Contact/', views.Contact, name='Contact'),
    path('Chat/', views.Chat, name='Chat'),
    path('login/', views.login_view, name='login'),
    path('Login', views.login_view, name='Login'),  # Support uppercase
    path('register/', views.register_view, name='register'),
]







 