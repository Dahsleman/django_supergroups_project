from django.forms import ModelForm
from .models import Group, Opening_hours

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

