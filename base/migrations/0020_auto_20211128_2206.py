# Generated by Django 3.2.8 on 2021-11-29 01:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_auto_20211128_2202'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='duration',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='startinterval',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='duration',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
