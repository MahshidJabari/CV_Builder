# Generated by Django 3.0.3 on 2020-02-25 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0009_auto_20200225_0409'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resume',
            options={'ordering': ('created_time', 'isActive'), 'verbose_name': 'Resume'},
        ),
    ]
