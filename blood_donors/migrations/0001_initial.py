# Generated by Django 5.1.4 on 2024-12-28 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodDonor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], default='O+', max_length=10)),
                ('district', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('location', models.CharField(choices=[('Nepal', 'Nepal'), ('Abroad', 'Abroad')], default='Nepal', max_length=20)),
                ('email_address', models.EmailField(max_length=254)),
            ],
        ),
    ]
