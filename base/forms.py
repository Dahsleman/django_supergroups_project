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

# class ShippingForm(forms.ModelForm):
#     class Meta:
#         model = ShippingInfo
#         fields = '__all__'

#     def fields_required(self, fields):
#     # """Used for conditionally marking fields as required."""
#         for field in fields:
#             if not self.cleaned_data.get(field, ''):
#                 msg = ValidationError("Select shipping destination")
#                 self.add_error(field, msg)

#     def clean(self):
#         shipping = self.cleaned_data.get('shipping')

#         if shipping:
#             self.fields_required(['shipping_destination'])
#         else:
#             self.cleaned_data['shipping_destination'] = ''

#         return self.cleaned_data

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