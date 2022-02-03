# Generated by Django 3.2.7 on 2022-02-03 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_tag_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='parent',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, related_name='children', to='base.tag'),
        ),
    ]