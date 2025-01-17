from django.shortcuts import render
from django.http import HttpResponse
from .models import Courses
# from .models import courses,testing_courses,networking_courses,other_courses
# Create your views here.
def index(request):
    return render(request,'index.html')
def course(request):
    details=Courses.objects.filter(parent_id=0)
    software=Courses.objects.filter(parent_id=1)
    testing=Courses.objects.filter(parent_id=2)
    networking=Courses.objects.filter(parent_id=3)
    other=Courses.objects.filter(parent_id=4)
    return render(request,'courses.html',{
        'details':details,
        'software':software,
        'testing':testing,
        'networking':networking,
        'other':other
        })
def course_details(request,id,parent_id):
    try:
        details=Courses.objects.get(id=id,parent_id=parent_id)
    except details.DoesNotExist:
        return HttpResponse('Error')
    return render(request,'course-details.html',{
        'details':details
    })

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def register(request):
    parents=Courses.objects.filter(parent_id=0)
    parent_child=[
        {
            'parent':parent,
            'children':Courses.objects.filter(parent_id=parent.id)
        }
        for parent in parents
    ]
    return render(request,'register.html',{
        'parents':parents,
        'parent_child':parent_child
    })