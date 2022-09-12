from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
from django.utils.translation import gettext_lazy as _



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

class Opening_hours_status(models.Model):
    status = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.status

class Opening_hours_time(models.Model):
    time = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.time

class Opening_hours_days(models.Model):
    days = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.days

class Opening_hours_notification(models.Model):
    notification = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.notification

class Opening_hours(models.Model):

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
        (1, '24 Hours'),
        (2, 'Set Open and Closed Time'),
    ]

    OPEN_TIME_CHOISES = [
        ('invalid',''),
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
        ))
    ]

    CLOSE_TIME_CHOISES = [
        ('invalid',''),
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
        ))
    ]

    NOTIFICATION_CHOISES = [
        ('on', 'On'),
        ('off', 'Off'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOISES,
        default='Open',
        help_text='''Select the status'''
        ) 
        
    time = models.FloatField(
        max_length=50,
        choices=TIME_CHOISES,
        default='24 Hours',
        help_text='''Select the time'''
        ) 

    # hide if time = 1
    open_time = models.CharField(
        max_length=50,
        choices=OPEN_TIME_CHOISES,
        default='invalid',
        help_text='''Select the open time''',
        null = True,
        blank=True
        ) 

    # hide if time = 1
    close_time = models.CharField(
        max_length=50,
        choices=CLOSE_TIME_CHOISES,
        default='invalid',
        help_text='''Select the close time''',
        null = True,
        blank=True
        ) 

    days = models.CharField(
        max_length=50,
        choices=DAYS_CHOISES,
        default='Everyday',
        help_text='''Select the days'''
        )

    notification = models.CharField(
        max_length=50,
        choices=NOTIFICATION_CHOISES,
        default='Off',
        help_text='''Select the notification'''
        )

    def __str__(self):
        return f'Opening_hours: {self.user}'


class Event(models.Model):
    YES_NO_CHOICES = [
    ('No', 'No'),
    ('Yes', 'Yes'),
    ]
    
    RECURRENCE_PATTERN_CHOICES = [
    ('---', '---'),
    ('Daily', 'Daily'),
    ('Weekly', 'Weekly'),
    ('Monthly', 'Monthly'),
    ('Yearly', 'Yearly'),
    ]

    event_name = models.CharField(
        max_length=70,
        help_text='''Enter a name for the event. This is a required field and is limited to 70 characters.'''
    )

    recurring_event = models.CharField(
        max_length=5,
        choices=YES_NO_CHOICES,
        default='No',
        help_text='''Is this a one off event or will it recur? Selecting Yes will open up additional fields.'''
    )
    
    recurrence_pattern = models.CharField(
        max_length=10,
        choices=RECURRENCE_PATTERN_CHOICES,
        default='---',
        help_text='''Select the recurrence pattern for this event.'''
    )

class Media(models.Model):
    MEDIA_CHOICES = [
    ('Audio', (
            ('vinyl', 'Vinyl'),
            ('cd', 'CD'),
        )
    ),
    ('Video', (
            ('vhs', 'VHS Tape'),
            ('dvd', 'DVD'),
        )
    ),
    ('unknown', 'Unknown'),
    ]
    
    Media_types = models.CharField(
        max_length=20,
        choices=MEDIA_CHOICES,
    )

class Student(models.Model):

    class YearInSchool(models.TextChoices):
        FRESHMAN = 'FR', _('Freshman')
        SOPHOMORE = 'SO', _('Sophomore')
        JUNIOR = 'JR', _('Junior')
        SENIOR = 'SR', _('Senior')
        GRADUATE = 'GR', _('Graduate')

    year_in_school = models.CharField(
        max_length=2,
        choices=YearInSchool.choices,
        default=YearInSchool.FRESHMAN,
    )

    def is_upperclass(self):
        return self.year_in_school in {
            self.YearInSchool.JUNIOR,
            self.YearInSchool.SENIOR,
        }

class Component(models.Model):

    COMPONENT_TYPE_CHOICES = (
        (1, 'k_v'),
        (2, 'pipe')
    )

    # circuit                     = models.ForeignKey('circuit.Circuit', related_name='components', on_delete=models.CASCADE)
    component_type              = models.IntegerField(default=1, choices = COMPONENT_TYPE_CHOICES)
    component_name              = models.CharField(max_length=200)
    branch_number_collectors    = models.IntegerField(default=4)

    # Hide if component_type==2 
    k_v                         = models.FloatField(default=1)

    # Hide if component_type==1
    DI                         = models.FloatField(default=0.025)
    length                      = models.FloatField(default=1)

    # Calculated properties
    branch_volumetric_flow_rate = models.FloatField(default=0)
    branch_mass_flow_rate       = models.FloatField(default=0)

    velocity                    = models.FloatField(default=0)
    reynolds                    = models.FloatField(default=0)
    friction_coefficient        = models.FloatField(default=0)
    pressure_loss               = models.FloatField(default=0)






    
