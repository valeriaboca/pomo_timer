from django.contrib import admin
from .models import User, UserSettings, Task

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'username', 'is_staff', 'is_active']
    search_fields = ['email', 'username']

@admin.register(UserSettings)
class UserSettingsAdmin(admin.ModelAdmin):
    list_display = ['user', 'pomodoro', 'short_break', 'long_break']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'completed_pomodoros', 'estimated_pomodoros', 'is_completed']
    list_filter = ['is_completed', 'created_at']
    search_fields = ['title']