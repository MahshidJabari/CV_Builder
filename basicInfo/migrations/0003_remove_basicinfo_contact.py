# Generated by Django 3.0.3 on 2020-02-23 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basicInfo', '0002_basicinfo_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basicinfo',
            name='contact',
        ),
    ]
