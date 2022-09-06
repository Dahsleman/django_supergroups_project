from django.forms import ModelForm
from .models import Availabilities, Group, Opening_hours

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
        exclude = ['admin','participants']

class AvailabilitiesForm(ModelForm):
    class Meta:
        model = Availabilities
        fields = '__all__'
        exclude = ['host','group']

class ParticipantsForm(ModelForm):
    class Meta:
        model = Group
        fields = ['participants']

class Opening_hours_Form(ModelForm):
    class Meta:
        model = Opening_hours
        fields = '__all__'
        exclude = ['user']

