# Generated by Django 4.1.7 on 2023-03-27 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mercadito', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='idProovedor',
            new_name='idProveedor',
        ),
    ]