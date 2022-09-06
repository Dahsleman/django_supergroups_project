from django.contrib import admin

from .models import Event, Group_type, Opening_hours, Opening_hours_days, Opening_hours_notification, Opening_hours_status, Opening_hours_time, Telegram, Group, Duration, Availabilities, StartInterval

admin.site.register(Event)
admin.site.register(Telegram)
admin.site.register(Group)
admin.site.register(Duration)
admin.site.register(Availabilities)
admin.site.register(StartInterval)
admin.site.register(Group_type)
admin.site.register(Opening_hours_status)
admin.site.register(Opening_hours_time)
admin.site.register(Opening_hours_days)
admin.site.register(Opening_hours_notification)
admin.site.register(Opening_hours)