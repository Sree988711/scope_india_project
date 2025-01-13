from django.shortcuts import render
from django.http import HttpResponse
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
def course_details(request,id,category):
    # details=courses.objects.get(id=id)
    category_map={
        'programming': courses,
        'testing': testing_courses,
        'networking': networking_courses,
        'other': other_courses,
    }
    model=category_map.get(category)

    try:
        details=model.objects.get(id=id)
    except model.DoesNotExist:
        return HttpResponse('Error')
    
    return render(request,'course-details.html',{
        'details':details
    })
def about(request):
    return render(request,'about.html')