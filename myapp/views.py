from django.shortcuts import render
from .models import courses,testing_courses
# Create your views here.
def index(request):
    return render(request,'index.html')
def course(request):
    details=courses.objects.all()
    testing=testing_courses.objects.all()
    return render(request,'courses.html',{
        'details':details,
        'testing':testing,
        })
