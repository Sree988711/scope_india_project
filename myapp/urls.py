from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.index,name='home'),
    path('courses/',views.course,name='courses'),
    # path('course-details/<str:category>/<int:id>/',views.course_details,name='detailx'),
    path('course-details/<int:parent_id>/<int:id>/',views.course_details,name='detailx'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login')
]
