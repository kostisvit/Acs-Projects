# Generated by Django 4.2 on 2024-01-29 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_alter_project_completion_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='completion_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]