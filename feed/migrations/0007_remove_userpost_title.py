# Generated by Django 2.0.5 on 2018-06-15 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0006_auto_20180615_1111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpost',
            name='title',
        ),
    ]
