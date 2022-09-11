from django.contrib import admin

from .models import *

admin.site.register(Telegram)
admin.site.register(Group)
admin.site.register(Group_type)
admin.site.register(Opening_hours_status)
admin.site.register(Opening_hours_time)
admin.site.register(Opening_hours_days)
admin.site.register(Opening_hours_notification)
admin.site.register(Opening_hours)
admin.site.register(Event)
admin.site.register(Media)
admin.site.register(Student)