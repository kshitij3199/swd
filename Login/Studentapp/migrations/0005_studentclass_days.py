# Generated by Django 2.0.1 on 2018-01-18 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Studentapp', '0004_auto_20180118_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentclass',
            name='days',
            field=models.IntegerField(default=0),
        ),
    ]