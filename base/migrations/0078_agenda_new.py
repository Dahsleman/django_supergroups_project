# Generated by Django 4.1 on 2022-12-01 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0077_alter_agenda_friday_alter_agenda_monday_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='new',
            field=models.BooleanField(null=True),
        ),
    ]
