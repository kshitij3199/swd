# Generated by Django 2.0.1 on 2018-01-18 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Studentapp', '0002_remove_studentclass_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentclass',
            name='startleave',
            field=models.IntegerField(default=0),
        ),
    ]
