from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Courses
from .models import Registration,Students,Callback
import random
from django.core.mail import EmailMessage
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.
def index(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        mobile=request.POST.get('phone')
        print(name,mobile)
        callback=Callback(
            name=name,
            mobile=mobile
        )
        callback.save()
        messages.success(request,'You will receive a call soon.')
        return redirect('register')

    return render(request,'index.html')
def course(request):
    details=Courses.objects.filter(parent_id=0)
    software=Courses.objects.filter(parent_id=1)
    testing=Courses.objects.filter(parent_id=2)
    networking=Courses.objects.filter(parent_id=3)
    other=Courses.objects.filter(parent_id=4)
    if request.method == 'POST':
        name=request.POST.get('name')
        mobile=request.POST.get('phone')
        print(name,mobile)
        callback=Callback(
            name=name,
            mobile=mobile
        )
        callback.save()
        messages.success(request,'You will receive a call soon.')
        return redirect('register')
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
    if request.method == 'POST':
        name=request.POST.get('name')
        mobile=request.POST.get('phone')
        print(name,mobile)
        callback=Callback(
            name=name,
            mobile=mobile
        )
        callback.save()
        messages.success(request,'You will receive a call soon.')
        return redirect('register')
    
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
        messages.success(request,'Registration Successful')
        return redirect('login')
    
    return render(request,'register.html',{
        'parents':parents,
        'parent_child':parent_child
    })
def login(request):
    email=request.session.get('reset_email','')

    if request.method == "POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            studentobj=Students.objects.get(email=email)

            if studentobj.password is None:  
                messages.error(request, "No password set for this account. Please reset your password.")
                return redirect('send-otp')
            
            if check_password(password,studentobj.password):
                request.session.flush()
                request.session['login_email']=email
                return redirect('dashboard')
            else:
                messages.error(request,'Invalid email or password..')
        except Students.DoesNotExist:
            messages.error(request,'User data Not found, Please Sign Up.')
    return render(request,'login.html',{
        'email':email
    })

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
    if request.method == 'POST':
        otp=request.POST.get('inputotp')
        print(otp)
        try:
            studentobj=Students.objects.get(email=email)
            if str(studentobj.otp) == otp:
                messages.success(request, 'OTP verified successfully.')
                return redirect('set-password')
            else:
                messages.error(request,'Invalid OTP. Please try again.')
        except Students.DoesNotExist:
            messages.error(request,'No data found')
    return render(request,'verify-otp.html',{
        'email':email
    })

def set_password(request):
    email=request.session.get('reset_email','')
    if request.method == "POST":
        pass_1=request.POST.get('inp_pass')
        pass_2=request.POST.get('con_pass')
        print(pass_1,pass_2)
        if pass_1 != pass_2:
            messages.error(request, "Passwords do not match. Please try again.")
        else:
            try:
                student=Students.objects.get(email=email)
                student.password=make_password(pass_1)
                student.save()
                messages.success(request, "Password set successfully! You can now log in.")
                return redirect('login')
            except Students.DoesNotExist:
                messages.error(request, "No account found with this email.")

    return render(request,'set-password.html',{
        'email':email
    })

def dashboard(request):
    email=request.session.get('login_email','')
    if not email:
        messages.error(request,'session not found, please do login')
        return redirect('login')
    
    student=Students.objects.get(email=email)
    try:
        details=Registration.objects.get(email=email)
    except Registration.DoesNotExist:
        messages.error(request,'Please register here before accessing Dashboard')
        return redirect('register')
    
    total_courses=21
    if student.additional_courses:
        completed_courses=len(student.additional_courses.split(',')) + 1
    else:
        completed_courses=1
    recommended_courses=Courses.objects.exclude(parent_id=0).order_by('?')[:6]
    return render(request,'dashboard.html',{
        'email':email,
        'details':details,
        'student':student,
        'completed_courses':completed_courses,
        'total_courses':total_courses,
        'recommended_courses':recommended_courses,
    })

def logout(request):
    request.session.flush()
    return redirect('login')

def view_profile(request):
    email=request.session.get('login_email','')
    if not email:
        messages.error(request,'session not found, please do login')
        return redirect('login')
    
    student=Students.objects.get(email=email)
    try:
        details=Registration.objects.get(email=email)
    except Registration.DoesNotExist:
        messages.error(request,'Please register here before accessing Dashboard')
        return redirect('register')
    return render(request,'view_profile.html',{
        'email':email,
        'details':details,
        'student':student
    })

def edit_profile(request):
    email=request.session.get('login_email','')
    if not email:
        messages.error(request,'session not found, please do login')
        return redirect('login')
    
    student=Students.objects.get(email=email)
    try:
        details=Registration.objects.get(email=email)
    except Registration.DoesNotExist:
        messages.error(request, "Profile not found.")
        return redirect('dashboard')

    if request.method == "POST":
        details.full_name=request.POST['full_name']
        details.dob=request.POST['dob']
        details.gender=request.POST['gender']
        details.mobile=request.POST['mobile']
        details.address=request.POST['address']
        details.save()

        if 'profile_image' in request.FILES:
            student.image=request.FILES['profile_image']
            student.save()
            
        messages.success(request,"Profile updated successfully!")
        return redirect('view_profile')

    return render(request,'edit_profile.html',{
        'details': details,
        'email':email,
        'student':student,
        })

def change_password(request):
    email = request.session.get('login_email','')
    if not email:
        messages.error(request,'session not found, please do login')
        return redirect('login')
    
    try:
        student = Students.objects.get(email=email)
    except Students.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect('login')

    if request.method == "POST":
        current_password=request.POST.get("current_password")
        new_password=request.POST.get("new_password")
        confirm_new_password=request.POST.get("confirm_new_password")

        if not student.password:
            messages.error(request,"Current password not set.")
            return redirect('change_password')

        if not check_password(current_password,student.password):
            messages.error(request, "Current password is incorrect.")
            return redirect('change_password')

        if new_password != confirm_new_password:
            messages.error(request,"Passwords does not match.")
            return redirect('change_password')

        student.password=make_password(new_password)
        student.save()
        messages.success(request,"Password changed successfully!")
        request.session.flush()
        return redirect('login')

    return render(request,'change_password.html', {
        'email': email,
        'student': student
    })
def view_courses(request):
    email=request.session.get('login_email','')
    if not email:
        messages.error(request,'session not found, please do login')
        return redirect('login')
    
    student=Students.objects.get(email=email)
    enrolled_courses=[]
    if student.additional_courses:
        course_names=student.additional_courses.split(',')
        enrolled_courses=Courses.objects.filter(courses_name__in=course_names)

    details=Registration.objects.get(email=email)
    return render(request,'view_courses.html',{
        'email':email,
        'student':student,
        'details':details,
        'enrolled_courses':enrolled_courses,
    })
def change_course(request):
    email=request.session.get('login_email','')
    if not email:
        messages.error(request,'session not found, please do login')
        return redirect('login')
    
    student=Students.objects.get(email=email)
    course=Courses.objects.exclude(parent_id=0)
    if request.method == 'POST':
        selected_course=request.POST.get('selected_course')
        if selected_course:
            student.add_course(selected_course)
            messages.success(request,f'Enrollment Successful:{selected_course}')
        return redirect('view_courses')
    return render(request,'change_course.html',{
        'email':email,
        'student':student,
        'course':course
    })