# Generated by Django 5.1.4 on 2025-01-01 16:09

import versatileimagefield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_alter_ourteam_vice_secretary_image_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourteam',
            name='treasurer_image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='treasurer/'),
        ),
    ]
