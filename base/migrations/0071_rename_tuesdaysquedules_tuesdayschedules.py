# Generated by Django 4.1 on 2022-11-27 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0070_rename_mondaysquedules_mondayschedules'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TuesdaySquedules',
            new_name='TuesdaySchedules',
        ),
    ]