# Generated by Django 5.0.4 on 2024-05-04 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='due_data',
            new_name='due_date',
        ),
    ]
