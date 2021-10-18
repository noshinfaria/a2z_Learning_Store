
from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.CourseList.as_view(), name='courses'),
    path('publish/', views.PublishCourse.as_view(), name='publish'),
    path('course_details/<slug:slug>/', views.course_details, name='course_details'),
    path('course_details/update/<slug:slug>/', views.CourseUpdateView.as_view(), name='course_update'),
    path('course_details/delete/<slug:slug>/', views.CourseDeleteView.as_view(), name='course_delete'),
    path('my_courses/', views.MyCourses.as_view(), name='my_courses'),
    path('question/<pk>/', views.question, name='question'),
]