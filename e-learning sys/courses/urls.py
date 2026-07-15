from django.urls import path

from . import views

app_name = "courses"

urlpatterns = [
    path("", views.course_list, name="course_list"),
    path("mine/", views.instructor_courses, name="instructor_courses"),
    path("create/", views.course_create, name="course_create"),
    path("<int:pk>/", views.course_detail, name="course_detail"),
    path("<int:pk>/enroll/", views.enroll, name="enroll"),
    path("<int:pk>/lessons/add/", views.lesson_create, name="lesson_create"),
]
