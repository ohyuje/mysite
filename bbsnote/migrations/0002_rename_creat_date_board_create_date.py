# Generated by Django 3.2.9 on 2021-11-15 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbsnote', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='creat_date',
            new_name='create_date',
        ),
    ]
