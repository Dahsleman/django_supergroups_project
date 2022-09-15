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
        exclude = ['user','timezone']

    def fields_required_time(self, fields):
    # """Used for conditionally marking fields as required."""
        for field in fields:
            if self.cleaned_data.get(field) == None:
                msg = ValidationError("Select Time")
                self.add_error(field, msg)

    def fields_required_open(self, fields):
    # """Used for conditionally marking fields as required."""
        for field in fields:
            if self.cleaned_data.get(field) == None:
                msg = ValidationError("Select open time")
                self.add_error(field, msg)

    def fields_required_close(self, fields):
    # """Used for conditionally marking fields as required."""
        for field in fields:
            if self.cleaned_data.get(field) == None:
                msg = ValidationError("Select close time")
                self.add_error(field, msg)

    def fields_required_error(self, fields):
    # """Used for conditionally marking fields as required."""
        for field in fields:
            msg = ValidationError("Open time and Close time cant be the same")
            self.add_error(field, msg)
            return 

    def fields_required_days(self, fields):
    # """Used for conditionally marking fields as required."""
        for field in fields:
            if self.cleaned_data.get(field) == None:
                msg = ValidationError("Select Days")
                self.add_error(field, msg)

    def fields_required_notification(self, fields):
    # """Used for conditionally marking fields as required."""
        for field in fields:
            if self.cleaned_data.get(field) == None:
                msg = ValidationError("Select Notification")
                self.add_error(field, msg)

    def clean(self):
        time = self.cleaned_data.get('time')
        open_time = self.cleaned_data.get('open_time')
        close_time = self.cleaned_data.get('close_time')
        days = self.cleaned_data.get('days')
        notification = self.cleaned_data.get('notification')

        if time == None:
            self.fields_required_time(['time'])

        elif time == 'set open and close time':
            if open_time == None:
                self.fields_required_open(['open_time'])
            if close_time == None and open_time != None:
                self.fields_required_close(['close_time'])
            if open_time == close_time and open_time != None and close_time != None:
                self.fields_required_error(['time'])

        elif days == None:
            self.fields_required_days(['days'])

        elif notification == None:
            self.fields_required_notification(['notification'])
        
        return self.cleaned_data

class TimezoneForm(ModelForm):
    class Meta:
        model = Opening_hours
        fields = ['timezone']

    def fields_required_timezone(self, fields):
    # """Used for conditionally marking fields as required."""
        for field in fields:
            if self.cleaned_data.get(field) == None:
                msg = ValidationError("Select Timezone")
                self.add_error(field, msg)

    def clean(self):
        timezone = self.cleaned_data.get('timezone')

        if timezone == None:
                self.fields_required_timezone(['timezone'])

class Voice_messagesForm(ModelForm):
    class Meta:
        model = Opening_hours
        fields = [
            'voice_messages',
            'voice_messages_notification'
        ]

    def fields_required_notification(self, fields):
    # """Used for conditionally marking fields as required."""
        for field in fields:
            if self.cleaned_data.get(field) == None:
                msg = ValidationError("Select notification")
                self.add_error(field, msg)

    def fields_required_voiceMessages(self, fields):
    # """Used for conditionally marking fields as required."""
        for field in fields:
            if self.cleaned_data.get(field) == None:
                msg = ValidationError("Select Voice Message type")
                self.add_error(field, msg)

    def clean(self):
        notification = self.cleaned_data.get('voice_messages_notification')
        voice_messages = self.cleaned_data.get('voice_messages')

        if notification == None:
                self.fields_required_notification(['voice_messages_notification'])

        if voice_messages == None:
                self.fields_required_voiceMessages(['voice_messages'])


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