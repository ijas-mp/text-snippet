# Generated by Django 3.2.12 on 2022-02-23 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='textdetails',
            old_name='tag_name',
            new_name='tag_id',
        ),
    ]
