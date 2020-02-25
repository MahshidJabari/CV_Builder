# Generated by Django 3.0.3 on 2020-02-24 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_auto_20200224_0328'),
        ('education', '0005_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='cv',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education_cv', to='resume.Resume'),
        ),
        migrations.AlterField(
            model_name='work',
            name='cv',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='works_cv', to='resume.Resume'),
        ),
    ]
