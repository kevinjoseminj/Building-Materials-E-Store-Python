# Generated by Django 3.1 on 2021-01-06 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0007_auto_20210105_1019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='description',
        ),
    ]
