from django.contrib import admin
from .models import ContactMessage, User

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)

# from django.contrib import admin
# from .models import User

# Register the User model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'full_name')  # Fields to display in the admin list view
    search_fields = ('username', 'email', 'full_name')  # Fields to enable search functionality