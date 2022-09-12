from django.forms import ModelForm
from .models import *
from django import forms
from django.core.exceptions import ValidationError

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
        exclude = ['admin','participants']

class ParticipantsForm(ModelForm):
    class Meta:
        model = Group
        fields = ['participants']

class Opening_hours_Form(ModelForm):
    class Meta:
        model = Opening_hours
        fields = '__all__'
        exclude = ['user']

    def fields_required_open(self, fields):
    # """Used for conditionally marking fields as required."""
        for field in fields:
            if self.cleaned_data.get(field) == 'invalid':
                msg = ValidationError("Select open time")
                self.add_error(field, msg)

    def fields_required_close(self, fields):
    # """Used for conditionally marking fields as required."""
        for field in fields:
            if self.cleaned_data.get(field) == 'invalid':
                msg = ValidationError("Select close time")
                self.add_error(field, msg)

    def fields_required_error(self, fields):
    # """Used for conditionally marking fields as required."""
        for field in fields:
            msg = ValidationError("Open time and Close time cant be the same")
            self.add_error(field, msg)
            return 

    def clean(self):
        time = self.cleaned_data.get('time')
        open_time = self.cleaned_data.get('open_time')
        close_time = self.cleaned_data.get('close_time')
        if time == 2:
            if open_time:
                self.fields_required_open(['open_time'])
            if close_time and open_time != 'invalid':
                self.fields_required_close(['close_time'])
            if open_time == close_time and open_time != 'invalid' and close_time != 'invalid':
                self.fields_required_error(['time'])

        return self.cleaned_data

class EventForm(ModelForm):
    """Event Staff Update view - allows staff to change event details"""
    class Meta:
        model = Event
        template_name = 'events/event_staff_summary_form.html'
        fields = [
                'event_name',
                'recurring_event',
                'recurrence_pattern',
        ]
        context_object_name = 'event'

class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = [
            'component_type',
            'component_name',
            'branch_number_collectors',
            'k_v',
            'DI',
            'length'
        ]