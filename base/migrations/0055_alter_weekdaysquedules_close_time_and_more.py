# Generated by Django 4.0 on 2022-09-24 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0054_alter_weekday_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weekdaysquedules',
            name='close_time',
            field=models.CharField(blank=True, choices=[('AM', (('0', '0h'), ('1', '1h'), ('2', '2h'), ('3', '3h'), ('4', '4h'), ('5', '5h'), ('6', '6h'), ('7', '7h'), ('8', '8h'), ('9', '9h'), ('10', '10h'), ('11', '11h'))), ('PM', (('12', '12h'), ('13', '13h'), ('14', '14h'), ('15', '15h'), ('16', '16h'), ('17', '17h'), ('18', '18h'), ('19', '19h'), ('20', '20h'), ('21', '21h'), ('22', '22h'), ('23', '23h')))], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='weekdaysquedules',
            name='open_time',
            field=models.CharField(blank=True, choices=[('AM', (('0', '0h'), ('1', '1h'), ('2', '2h'), ('3', '3h'), ('4', '4h'), ('5', '5h'), ('6', '6h'), ('7', '7h'), ('8', '8h'), ('9', '9h'), ('10', '10h'), ('11', '11h'))), ('PM', (('12', '12h'), ('13', '13h'), ('14', '14h'), ('15', '15h'), ('16', '16h'), ('17', '17h'), ('18', '18h'), ('19', '19h'), ('20', '20h'), ('21', '21h'), ('22', '22h'), ('23', '23h')))], max_length=50, null=True),
        ),
    ]
