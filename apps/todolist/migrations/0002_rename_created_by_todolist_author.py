# Generated by Django 4.2 on 2024-01-22 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='created_by',
            new_name='author',
        ),
    ]
