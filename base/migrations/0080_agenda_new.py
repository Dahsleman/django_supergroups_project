# Generated by Django 4.1 on 2022-12-01 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0079_remove_agenda_new_alter_agenda_friday_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='new',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
