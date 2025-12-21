from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='settings')
    pomodoro = models.IntegerField(default=25)
    short_break = models.IntegerField(default=5)
    long_break = models.IntegerField(default=15)
    auto_start_break = models.BooleanField(default=False)
    auto_start_pomodoro = models.BooleanField(default=False)
    long_break_interval = models.IntegerField(default=4)

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    estimated_pomodoros = models.IntegerField(default=1)
    completed_pomodoros = models.IntegerField(default=0)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

# Sessions
# Projects
# DailyStats