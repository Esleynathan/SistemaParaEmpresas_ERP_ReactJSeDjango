# Generated by Django 4.2.15 on 2024-08-22 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_employee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enterprise',
            old_name='nome',
            new_name='name',
        ),
    ]
