# Generated by Django 4.2 on 2024-01-25 11:20

from django.db import migrations, models
import project.models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='projectfile',
            name='attachment',
            field=models.FileField(upload_to=project.models.custom_upload_path),
        ),
    ]
