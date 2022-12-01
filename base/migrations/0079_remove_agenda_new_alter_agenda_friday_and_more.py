# Generated by Django 4.1 on 2022-12-01 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0078_agenda_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agenda',
            name='new',
        ),
        migrations.AlterField(
            model_name='agenda',
            name='friday',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='monday',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='saturday',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='sunday',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='thursday',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='tuesday',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='wednesday',
            field=models.BooleanField(default=True),
        ),
    ]