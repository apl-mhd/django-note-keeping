# Generated by Django 3.2.7 on 2022-02-03 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20220202_1117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='ordering',
        ),
    ]
