from django.forms import ModelForm
from .models import Group, Settings, Agenda, MondaySquedules
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
        model = Settings
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
        model = Settings
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
        model = Settings
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


class AgendaForm(ModelForm):

    class Meta:
        model = Agenda
        fields = '__all__'
        exclude = [
            'user'
        ]

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['monday'].label = ''

class MondayScheduleForm(ModelForm):

    class Meta:
        model = MondaySquedules
        fields = [
            'start_time',
            'end_time'
        ]
        verbose_name_plural = 'Monday'

    # def clean(self):
    #     start_time = self.cleaned_data.get('start_time')
    #     end_time = self.cleaned_data.get('end_time')
        

    #     if start_time == None:
    #         self.start_list.clear()
    #         self.end_list.clear()
            
    #         raise ValidationError ({'start_time':('select start time')}) 
        
    #     elif end_time == None:
    #         self.start_list.clear()
    #         self.end_list.clear()
            
    #         raise ValidationError ({'end_time':('select end time')}) 

    #     else:
    #         start_time = int(start_time)
    #         end_time = int(end_time)

    #     if end_time <= start_time:
    #         self.start_list.clear()
    #         self.end_list.clear()
            
    #         raise ValidationError ({'end_time':('must be bigger than start time')})

        # if agenda == None:

        #     num = len(self.start_list)
                   
        #     if num == 0:
        #         self.start_list.append(start_time)
        #         self.end_list.append(end_time)
        #         self.var_list.append(self.w)
        #     else:
                
        #         self.q = self.var_list[0]
        #         while self.q >= 0:
                    
        #             if start_time == self.start_list[self.q]:
        #                 self.start_list.clear()
        #                 self.end_list.clear()
        #                 self.var_list.clear()
        #                 raise ValidationError ({'start_time':('conflict')}) 
                    
        #             if start_time > self.start_list[self.q] and start_time < self.end_list[self.q]:
        #                 self.start_list.clear()
        #                 self.end_list.clear()
        #                 self.var_list.clear()
        #                 raise ValidationError ({'start_time':('conflict')}) 
                    
        #             if end_time > self.start_list[self.q] and end_time < self.end_list[self.q]:
        #                 self.start_list.clear()
        #                 self.end_list.clear()
        #                 self.var_list.clear()
        #                 raise ValidationError ({'end_time':('conflict')}) 
        #             else:
        #                 self.q = self.q - 1
                
        #         self.start_list.append(start_time)
        #         self.end_list.append(end_time)
        #         self.w = self.var_list[0]
        #         self.w += 1
        #         self.var_list[0] = self.w
        


