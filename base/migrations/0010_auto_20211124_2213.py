# Generated by Django 3.2.8 on 2021-11-25 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_auto_20211124_2157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='description',
        ),
        migrations.RemoveField(
            model_name='event',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='event',
            name='group',
        ),
        migrations.RemoveField(
            model_name='event',
            name='name',
        ),
        migrations.RemoveField(
            model_name='event',
            name='user',
        ),
        migrations.RemoveField(
            model_name='group',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='group',
            name='created',
        ),
        migrations.RemoveField(
            model_name='group',
            name='description',
        ),
        migrations.RemoveField(
            model_name='group',
            name='name',
        ),
        migrations.RemoveField(
            model_name='group',
            name='updated',
        ),
    ]
