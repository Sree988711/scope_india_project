# Generated by Django 5.1.4 on 2025-01-12 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_courses_course_duration_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='course_contents',
            field=models.TextField(blank=True),
        ),
    ]