# Generated by Django 4.0 on 2022-09-22 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('base', '0051_remove_event_recurrence_pattern_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weekday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Enter a name for the event. This is a required field and is limited to 70 characters.', max_length=70, null=True)),
                ('availability', models.CharField(blank=True, choices=[('available', 'Available'), ('unavailable', 'Unavailable')], default='available', max_length=50, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='WeekdaySquedules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_time', models.CharField(blank=True, choices=[('AM', (('0', '0h'), ('1', '1h'), ('2', '2h'), ('3', '3h'), ('4', '4h'), ('5', '5h'), ('6', '6h'), ('7', '7h'), ('8', '8h'), ('9', '9h'), ('10', '10h'), ('11', '11h'))), ('PM', (('12', '12h'), ('13', '13h'), ('14', '14h'), ('15', '15h'), ('16', '16h'), ('17', '17h'), ('18', '18h'), ('19', '19h'), ('20', '20h'), ('21', '21h'), ('22', '22h'), ('23', '23h')))], default='9', max_length=50, null=True)),
                ('close_time', models.CharField(blank=True, choices=[('AM', (('0', '0h'), ('1', '1h'), ('2', '2h'), ('3', '3h'), ('4', '4h'), ('5', '5h'), ('6', '6h'), ('7', '7h'), ('8', '8h'), ('9', '9h'), ('10', '10h'), ('11', '11h'))), ('PM', (('12', '12h'), ('13', '13h'), ('14', '14h'), ('15', '15h'), ('16', '16h'), ('17', '17h'), ('18', '18h'), ('19', '19h'), ('20', '20h'), ('21', '21h'), ('22', '22h'), ('23', '23h')))], default='17', max_length=50, null=True)),
                ('weekday', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.weekday')),
            ],
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]