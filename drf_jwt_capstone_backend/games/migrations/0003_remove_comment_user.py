# Generated by Django 3.1 on 2021-11-24 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20211119_0932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]
