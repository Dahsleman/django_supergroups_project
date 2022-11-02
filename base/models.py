from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
import pytz
from django.urls import reverse
from django.core.exceptions import ValidationError
# from base.forms import MondayScheduleForm

class Telegram(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    telegram_id = models.IntegerField(null=True, blank=True)
    token = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Token:{self.token}"

class Group_type(models.Model):
    type = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.type

class Group(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    type = models.ForeignKey(Group_type, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name

class Settings(models.Model):

    STATUS_CHOISES = [
        ('open', 'Open'),
        ('permanently closed', 'Permanently Closed'),
    ]

    DAYS_CHOISES = [
        ('everyday', 'Everyday'),
        ('weekdays', 'Weekdays'),
        ('weekends', 'Weekends'),
    ]

    TIME_CHOISES = [
        ('24 hours', '24 Hours'),
        ('set open and close time', 'Set Open and Close Time'),
    ]

    OPEN_TIME_CHOISES = [
        ('AM', (
            ('0', '0h'),
            ('1', '1h'),
            ('2', '2h'),
            ('3', '3h'),
            ('4', '4h'),
            ('5', '5h'),
            ('6', '6h'),
            ('7', '7h'),
            ('8', '8h'),
            ('9', '9h'),
            ('10', '10h'),
            ('11', '11h'),
        )),
        ('PM', (
            ('12', '12h'),
            ('13', '13h'),
            ('14', '14h'),
            ('15', '15h'),
            ('16', '16h'),
            ('17', '17h'),
            ('18', '18h'),
            ('19', '19h'),
            ('20', '20h'),
            ('21', '21h'),
            ('22', '22h'),
            ('23', '23h'),
        ))
    ]

    CLOSE_TIME_CHOISES = [
        ('AM', (
            ('0', '0h'),
            ('1', '1h'),
            ('2', '2h'),
            ('3', '3h'),
            ('4', '4h'),
            ('5', '5h'),
            ('6', '6h'),
            ('7', '7h'),
            ('8', '8h'),
            ('9', '9h'),
            ('10', '10h'),
            ('11', '11h'),
        )),
        ('PM', (
            ('12', '12h'),
            ('13', '13h'),
            ('14', '14h'),
            ('15', '15h'),
            ('16', '16h'),
            ('17', '17h'),
            ('18', '18h'),
            ('19', '19h'),
            ('20', '20h'),
            ('21', '21h'),
            ('22', '22h'),
            ('23', '23h'),
        ))
    ]

    NOTIFICATION_CHOISES = [
        ('on', 'On'),
        ('off', 'Off'),
    ]

    VOICE_MESSAGES_CHOISES = [
        ('inactivated','Inactivate'),
        ('activated','Activate')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOISES,
        default='Open',
        help_text='''Select the status'''
        ) 
        
    time = models.CharField(
        max_length=50,
        choices=TIME_CHOISES,
        default='24 Hours',
        help_text='''Select the time''',
        blank=True,
        null=True
        ) 

    open_time = models.CharField(
        max_length=50,
        choices=OPEN_TIME_CHOISES,
        default='invalid',
        help_text='''Select the open time''',
        null=True

        ) 

    close_time = models.CharField(
        max_length=50,
        choices=CLOSE_TIME_CHOISES,
        default='invalid',
        help_text='''Select the close time''',
        null=True
        ) 

    days = models.CharField(
        max_length=50,
        choices=DAYS_CHOISES,
        default='Everyday',
        help_text='''Select the days''',
        blank=True,
        null=True
        )

    notification = models.CharField(
        max_length=50,
        choices=NOTIFICATION_CHOISES,
        default='Off',
        help_text='''Select the notification''',
        blank=True,
        null=True
        )

    timezone = models.CharField(
        max_length=128, 
        choices=[(tz, tz) for tz in pytz.common_timezones],
        default='America/Sao_Paulo',
        blank=True,
        null=True
        )

    voice_messages = models.CharField(
        max_length=50,
        choices=VOICE_MESSAGES_CHOISES,
        default='Inactivate',
        blank=True,
        null=True
        )

    voice_messages_notification = models.CharField(
        max_length=10,
        choices=NOTIFICATION_CHOISES,
        default='Off',
        blank=True,
        null=True
        )

    def __str__(self):
        return f'Opening_hours: {self.user}'






class Agenda(models.Model):

    INCREMENTS_CHOISES = [
        ('15','15 min'), ('30','30 min'), ('45', '45 min'), ('60', '60 min')
    ]

    class Meta:
        # verbose_name = 'Monday'
        verbose_name_plural = 'agenda'

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(
        max_length=70,
        blank=True,
        null=True
    )

    increments = models.CharField(
        max_length=50,
        choices=INCREMENTS_CHOISES,
        default='30 min',
        null=True
        ) 

    monday = models.BooleanField(
        default=True,     
    ) 

    def __str__(self):
        return f'{self.user} - {self.name}'

    def get_list_url():
        return reverse('telegram-agenda-list')

    def get_absolute_url(self):
        return reverse('telegram-agenda-detail', kwargs={'id':self.id})

    def get_edit_url(self):
        return reverse('telegram-agenda-update', kwargs={'id':self.id})

    def get_delete_url(self):
        return reverse('telegram-agenda-delete', kwargs={'id':self.id})

    def get_hx_url(self):
        return reverse("hx-telegram-agenda-detail", kwargs={"id": self.id})

    def get_monday_schedules_children(self):
        return self.mondaysquedules_set.all()

    def get_user_id(self):
        return self.user.id


class MondaySquedules(models.Model):

    class Meta:
        verbose_name = 'Monday'
        verbose_name_plural = 'monday'

    OPEN_TIME_CHOISES = [
        ('AM', (('0', '0h'),('1', '1h'),('2', '2h'),('3', '3h'),('4', '4h'),('5', '5h'),('6', '6h'),('7', '7h'),('8', '8h'),('9', '9h'),('10', '10h'),('11', '11h'),)),
        ('PM', (('12', '12h'),('13', '13h'),('14', '14h'),('15', '15h'),('16', '16h'),('17', '17h'),('18', '18h'),('19', '19h'),('20', '20h'),('21', '21h'),('22', '22h'),('23', '23h'),))
    ]

    CLOSE_TIME_CHOISES = [
        ('AM', (('0', '0h'),('1', '1h'),('2', '2h'),('3', '3h'),('4', '4h'),('5', '5h'),('6', '6h'),('7', '7h'),('8', '8h'),('9', '9h'),('10', '10h'),('11', '11h'),)),
        ('PM', (('12', '12h'),('13', '13h'),('14', '14h'),('15', '15h'),('16', '16h'),('17', '17h'),('18', '18h'),('19', '19h'),('20', '20h'),('21', '21h'),('22', '22h'),('23', '23h'),))
    ]

    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE, null=True, blank=True)

    available = models.BooleanField(
        default=True,     
    )

    start_time = models.CharField(
        max_length=50,
        choices=OPEN_TIME_CHOISES,
        # blank=True,
        null=True,
        ) 

    end_time = models.CharField(
        max_length=50,
        choices=CLOSE_TIME_CHOISES,
        # blank=True,
        null=True,
        )  
    
    def __str__(self):
        return f'{self.agenda} availabilities'

    def get_absolute_url(self):
        return self.agenda.get_absolute_url()

    def get_delete_monday_url(self):
        kwargs = {
            "parent_id":self.agenda.id,
            "id":self.id
        }
        return reverse('monday-delete', kwargs=kwargs)

    def get_hx_edit_url(self):
        kwargs = {
            "parent_id":self.agenda.id,
            "id":self.id
        }
        return reverse('hx-monday-detail', kwargs=kwargs)

    def get_hx_create_url(self):
        return reverse("hx-monday-create", kwargs={"parent_id":self.agenda.id})


    
        

    


            

        





    
