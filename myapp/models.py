from django.db import models

# Create your models here.
class courses(models.Model):
    course_name=models.CharField(max_length=50)
    class Meta:
        verbose_name_plural='Software Courses'
    def __str__(self):
        return self.course_name
    
class testing_courses(models.Model):
    course_name=models.CharField(max_length=50)
    class Meta:
        verbose_name_plural='Testing Courses'
    def __str__(self):
        return self.course_name

class networking_courses(models.Model):
    course_name=models.CharField(max_length=50)
    class Meta:
        verbose_name_plural='Networking Courses'
    def __str__(self):
        return self.course_name

class other_courses(models.Model):
    course_name=models.CharField(max_length=50)
    class Meta:
        verbose_name_plural='Other Courses'
    def __str__(self):
        return self.course_name
