from django.shortcuts import render
from .models import courses,testing_courses,networking_courses,other_courses
# Create your views here.
def index(request):
    return render(request,'index.html')
def course(request):
    details=courses.objects.all()
    testing=testing_courses.objects.all()
    networking=networking_courses.objects.all()
    other=other_courses.objects.all()
    return render(request,'courses.html',{
        'details':details,
        'testing':testing,
        'networking':networking,
        'other':other
        })
def course_details(request):
    return render(request,'course-details.html')
