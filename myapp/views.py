from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Courses
from .models import Registration,Students
import random
from django.core.mail import EmailMessage
from django.contrib import messages
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

    if request.method == 'POST':
        # Collect data from the form
        full_name = request.POST.get('full_name')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        qualification = request.POST.get('qualification')
        course = request.POST.get('course')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        guardian_mobile = request.POST.get('guardian_mobile')
        mode = request.POST.get('mode')
        location = request.POST.get('location')
        guardian_name = request.POST.get('guardian_name')
        guardian_occupation = request.POST.get('guardian_occupation')
        preferred_timings = request.POST.getlist('preferred_timings')
        address = request.POST.get('address')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        pin = request.POST.get('pin')

        registration = Registration(
            full_name=full_name,
            dob=dob,
            gender=gender,
            qualification=qualification,
            course=course,
            mobile=mobile,
            email=email,
            guardian_mobile=guardian_mobile,
            mode=mode,
            location=location,
            guardian_name=guardian_name,
            guardian_occupation=guardian_occupation,
            preferred_timings=", ".join(preferred_timings),
            address=address,
            country=country,
            state=state,
            city=city,
            pin=pin
        )
        registration.save()
        return HttpResponse("Registration Successful")
    
    return render(request,'register.html',{
        'parents':parents,
        'parent_child':parent_child
    })
def login(request):
    return render(request,'login.html')

def send_otp(request):
    if request.method == "POST":
        email=request.POST.get('inputemail')
        otpgen=random.randrange(1000,9999)
        #sendingotp
        subject='Scope India OTP'
        message='Your otp is {}'.format(otpgen)
        frommail='988711test40@gmail.com'
        tomail=email
        mail=EmailMessage(subject,message,frommail,[tomail])
        mail.send()
        print(email,otpgen)
        messages.success(request,'OTP Sent Successfully to {}'.format(email))
        #dbsave
        studentobj,created=Students.objects.update_or_create(
            email=email,
            defaults={'otp':otpgen}
        )
        #session
        request.session['reset_email']=email

        return redirect('verify-otp')
    return render(request,'send-otp.html')

def verify_otp(request):
    email=request.session.get('reset_email','')
    return render(request,'verify-otp.html',{
        'email':email
    })

def set_password(request):
    email=request.session.get('reset_email','')
    return render(request,'set-password.html',{
        'email':email
    })
