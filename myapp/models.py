from django.db import models

# Create your models here.
class courses(models.Model):
    course_name=models.CharField(max_length=50)
    course_details_name=models.CharField(max_length=50,default='CourseX')
    course_duration=models.CharField(max_length=50,default='4 months course + 3 months on the Job Training')
    course_contents=models.TextField(blank=True)
    class Meta:
        verbose_name_plural='Software Courses'
    def __str__(self):
        return self.course_name
    def get_course_contents(self):
        return self.course_contents.split(",") if self.course_contents else []
    
class testing_courses(models.Model):
    course_name=models.CharField(max_length=50)
    course_details_name=models.CharField(max_length=50,default='CourseX')
    course_duration=models.CharField(max_length=50,default='4 months course + 3 months on the Job Training')
    testing_contents=models.TextField(blank=True)
    class Meta:
        verbose_name_plural='Testing Courses'
    def __str__(self):
        return self.course_name
    def get_course_contents(self):
        return self.testing_contents.split(",") if self.testing_contents else []

class networking_courses(models.Model):
    course_name=models.CharField(max_length=50)
    course_details_name=models.CharField(max_length=50,default='CourseX')
    course_duration=models.CharField(max_length=50,default='4 months course + 3 months on the Job Training')
    networking_contents=models.TextField(blank=True)
    class Meta:
        verbose_name_plural='Networking Courses'
    def __str__(self):
        return self.course_name
    def get_course_contents(self):
        return self.networking_contents.split(",") if self.networking_contents else []

class other_courses(models.Model):
    course_name=models.CharField(max_length=50)
    course_details_name=models.CharField(max_length=50,default='CourseX')
    course_duration=models.CharField(max_length=50,default='4 months course + 3 months on the Job Training')
    other_contents=models.TextField(blank=True)
    class Meta:
        verbose_name_plural='Other Courses'
    def __str__(self):
        return self.course_name
    def get_course_contents(self):
        return self.other_contents.split(',') if self.other_contents else []
