from django.contrib import admin
from base.forms import MondayScheduleForm
from .models import *
from django.forms.models import BaseInlineFormSet

admin.site.register(Telegram)
admin.site.register(Group_type)
admin.site.register(Settings)


class WeekdaySquedulesInlineFormSet(BaseInlineFormSet):                  
    def save_new_objects(self, commit=True):
        saved_instances = super(WeekdaySquedulesInlineFormSet, self).save_new_objects(commit)
        if commit:
            MondayScheduleForm.start_list.clear()
            MondayScheduleForm.end_list.clear()
            MondayScheduleForm.var_list.clear()
            return saved_instances

class MondaySquedulesInline(admin.TabularInline):
    model = MondaySchedules
    extra = 0
    form = MondayScheduleForm
    # formset = WeekdaySquedulesInlineFormSet
    exclude = [
        'available'
    ]

class TuesdaySquedulesInline(admin.TabularInline):
    model = TuesdaySchedules
    extra = 0
    form = MondayScheduleForm
    # formset = WeekdaySquedulesInlineFormSet
    exclude = [
        'available'
    ]  


class AgendaAdmin(admin.ModelAdmin):
    inlines = [
        MondaySquedulesInline,
        TuesdaySquedulesInline,
    ]
    
    list_display = ['user', 'name']
    raw_id_fields = ['user']


admin.site.register(Agenda, AgendaAdmin)

admin.site.register(MondaySchedules)