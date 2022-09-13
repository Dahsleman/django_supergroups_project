# Generated by Django 4.0 on 2022-09-13 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0040_alter_opening_hours_close_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opening_hours',
            name='close_time',
            field=models.CharField(blank=True, choices=[('invalid', ''), ('AM', (('0', '0h'), ('1', '1h'), ('2', '2h'), ('3', '3h'), ('4', '4h'), ('5', '5h'), ('6', '6h'), ('7', '7h'), ('8', '8h'), ('9', '9h'), ('10', '10h'), ('11', '11h'))), ('PM', (('12', '12h'), ('13', '13h'), ('14', '14h'), ('15', '15h'), ('16', '16h'), ('17', '17h'), ('18', '18h'), ('19', '19h'), ('20', '20h'), ('21', '21h'), ('22', '22h'), ('23', '23h')))], default='invalid', help_text='Select the close time', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='opening_hours',
            name='days',
            field=models.CharField(blank=True, choices=[('everyday', 'Everyday'), ('weekdays', 'Weekdays'), ('weekends', 'Weekends')], default='Everyday', help_text='Select the days', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='opening_hours',
            name='notification',
            field=models.CharField(blank=True, choices=[('on', 'On'), ('off', 'Off')], default='Off', help_text='Select the notification', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='opening_hours',
            name='open_time',
            field=models.CharField(blank=True, choices=[('invalid', ''), ('AM', (('0', '0h'), ('1', '1h'), ('2', '2h'), ('3', '3h'), ('4', '4h'), ('5', '5h'), ('6', '6h'), ('7', '7h'), ('8', '8h'), ('9', '9h'), ('10', '10h'), ('11', '11h'))), ('PM', (('12', '12h'), ('13', '13h'), ('14', '14h'), ('15', '15h'), ('16', '16h'), ('17', '17h'), ('18', '18h'), ('19', '19h'), ('20', '20h'), ('21', '21h'), ('22', '22h'), ('23', '23h')))], default='invalid', help_text='Select the open time', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='opening_hours',
            name='time',
            field=models.CharField(blank=True, choices=[('24 hours', '24 Hours'), ('set open and close time', 'Set Open and Close Time')], default='24 Hours', help_text='Select the time', max_length=50, null=True),
        ),
    ]
