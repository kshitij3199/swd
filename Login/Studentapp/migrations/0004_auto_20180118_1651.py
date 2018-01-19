# Generated by Django 2.0.1 on 2018-01-18 11:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Studentapp', '0003_studentclass_startleave'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentclass',
            name='startleave',
        ),
        migrations.AddField(
            model_name='studentclass',
            name='approval',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentclass',
            name='arrival_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='studentclass',
            name='departure_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
