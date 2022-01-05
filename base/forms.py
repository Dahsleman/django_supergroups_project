from django.forms import ModelForm
from .models import Availabilities, Group

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

