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

class Registration(models.Model):
    full_name = models.CharField(max_length=255)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    qualification = models.CharField(max_length=255, blank=True, null=True)
    course = models.CharField(max_length=255,blank=True, null=True)
    mobile = models.CharField(max_length=15,blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    guardian_mobile = models.CharField(max_length=15, blank=True, null=True)
    mode = models.CharField(max_length=50,blank=True, null=True)
    location = models.CharField(max_length=100,blank=True, null=True)
    guardian_name = models.CharField(max_length=255, blank=True, null=True)
    guardian_occupation = models.CharField(max_length=255, blank=True, null=True)
    preferred_timings = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    pin = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.full_name

class Students(models.Model):
    email=models.EmailField(max_length=50,null=False,blank=False,unique=True)
    otp=models.IntegerField(null=False,blank=False)
    password=models.TextField(null=True)
    image=models.ImageField(upload_to="profile_images/",null=True,blank=True)
    additional_courses = models.TextField(null=True, blank=True)

    def add_course(self,course_name):
        if self.additional_courses:
            courses=self.additional_courses.split(';')
            if course_name not in courses:
                courses.append(course_name)
                self.additional_courses= ';'.join(courses)
        else:
            self.additional_courses=course_name
        self.save()

    def __str__(self):
        return self.email

class Callback(models.Model):
    name=models.CharField(max_length=50,blank=False,null=False)
    mobile=models.CharField(max_length=15,blank=False,null=False)

    def __str__(self):
        return self.name