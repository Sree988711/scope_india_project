# Generated by Django 5.1.4 on 2025-02-18 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_students_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
    ]
