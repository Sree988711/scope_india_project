# Generated by Django 5.1.4 on 2025-01-16 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_courses_content_courses_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='courses',
            name='duration',
            field=models.TextField(default='4 months course + 3 months on the Job Training', null=True),
        ),
    ]
