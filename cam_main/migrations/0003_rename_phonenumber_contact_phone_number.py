# Generated by Django 4.1.1 on 2022-10-07 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cam_main', '0002_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='phonenumber',
            new_name='phone_number',
        ),
    ]