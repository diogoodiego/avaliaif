# Generated by Django 4.2.3 on 2023-07-21 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avaliaif', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='nome',
            new_name='name',
        ),
    ]