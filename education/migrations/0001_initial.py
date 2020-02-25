# Generated by Django 3.0.3 on 2020-02-23 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('educationLevel', models.CharField(max_length=64, null=True)),
                ('fieldOfStudy', models.CharField(max_length=64, null=True)),
                ('branch', models.CharField(max_length=128, null=True)),
                ('instituteTitle', models.CharField(max_length=128, null=True)),
                ('gpa', models.CharField(max_length=128, null=True)),
                ('country', models.CharField(max_length=64, null=True)),
                ('state', models.CharField(max_length=64, null=True)),
                ('city', models.CharField(max_length=128, null=True)),
                ('address', models.CharField(max_length=512, null=True)),
                ('entrance', models.CharField(max_length=8, null=True)),
                ('graduateYear', models.CharField(max_length=8, null=True)),
                ('currently_studying', models.BooleanField()),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='resume.Resume')),
            ],
            options={
                'verbose_name': 'Education',
                'ordering': ('created_time',),
            },
        ),
    ]
