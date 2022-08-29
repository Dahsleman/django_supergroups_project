from django.contrib import admin

from .models import Event, Group_type, Telegram, Group, Duration, Availabilities, StartInterval

admin.site.register(Event)
admin.site.register(Telegram)
admin.site.register(Group)
admin.site.register(Duration)
admin.site.register(Availabilities)
admin.site.register(StartInterval)
admin.site.register(Group_type)
