from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('courses/',views.course,name='courses'),
    # path('course-details/<str:category>/<int:id>/',views.course_details,name='detailx'),
    path('course-details/<int:parent_id>/<int:id>/',views.course_details,name='detailx'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('send-otp/',views.send_otp,name='send-otp'),
    path('set-password/',views.set_password,name='set-password'),
    path('verify-otp/',views.verify_otp,name='verify-otp'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.logout,name='logout'),
    path('view-profile/',views.view_profile,name='view_profile'),
    path('edit-profile/',views.edit_profile,name='edit_profile'),
    path('change-password/',views.change_password,name='change_password'),
    path('view-courses/',views.view_courses,name='view_courses'),
    path('change-course/',views.change_course,name='change_course'),
    path('delete-course/<int:course_id>/',views.delete_course,name='delete_course'),
]
