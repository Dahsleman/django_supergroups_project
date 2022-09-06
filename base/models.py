from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL

class Telegram(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    telegram_id = models.IntegerField(null=True, blank=True)
    token = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Token:{self.token}"

class Group_type(models.Model):
    type = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.type

class Group(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    type = models.ForeignKey(Group_type, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name

class Opening_hours_status(models.Model):
    status = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.status

class Opening_hours_time(models.Model):
    time = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.time

class Opening_hours_days(models.Model):
    days = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.days

class Opening_hours_notification(models.Model):
    notification = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.notification

class Opening_hours(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    status = models.ForeignKey(Opening_hours_status, on_delete=models.CASCADE, null=True) 
    time = models.ForeignKey(Opening_hours_time, on_delete=models.CASCADE, null=True)
    days = models.ForeignKey(Opening_hours_days, on_delete=models.CASCADE, null=True)
    notification = models.ForeignKey(Opening_hours_notification, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Opening_hours: {self.user}'




    
