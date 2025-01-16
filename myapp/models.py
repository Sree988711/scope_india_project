from django.db import models

# Create your models here.

# Transition to mysql

from django.db import models

class Courses(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    courses_name = models.TextField(null=False)
    parent_id = models.IntegerField(null=False)
    details_name = models.TextField(null=True)
    duration = models.TextField(default='4 months course + 3 months on the Job Training',null=True)
    content = models.TextField(null=True)

    def __str__(self):
        return self.courses_name
    def get_course_contents(self):
        return self.content.split(';') if self.content else []
