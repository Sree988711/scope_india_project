from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('courses/',views.course,name='courses'),
    path('course-details/',views.course_details,name='detail'),
]
