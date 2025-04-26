# filepath: [urls.py](http://_vscodecontentref_/1)
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Homepage.urls')),
    path('chat-page/', views.chat_page, name='chat_page'),
    path('api/chat/', views.gemini_chat_api, name='gemini_chat_api'),
    path('api/models/', views.list_models, name='list_models'),
]