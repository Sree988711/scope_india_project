# Generated by Django 5.1.4 on 2025-01-23 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_rename_student_name_registration_mode_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='address',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='city',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='country',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='course',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='email',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='guardian_mobile',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='guardian_name',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='guardian_occupation',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='location',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='mode',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='pin',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='preferred_timings',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='qualification',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='state',
        ),
    ]
