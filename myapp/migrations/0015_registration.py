# Generated by Django 5.1.4 on 2025-01-23 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_alter_courses_content_alter_courses_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
            ],
        ),
    ]
