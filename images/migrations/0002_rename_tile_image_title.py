# Generated by Django 4.1.8 on 2023-04-29 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='tile',
            new_name='title',
        ),
    ]
