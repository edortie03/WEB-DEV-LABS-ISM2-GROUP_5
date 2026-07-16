from django.urls import path

from . import views

app_name = "progress"

urlpatterns = [
    path("course/<int:course_pk>/", views.course_progress, name="course_progress"),
    path("lesson/<int:lesson_pk>/complete/", views.mark_complete, name="mark_complete"),
    path("course/<int:course_pk>/certificate/", views.certificate_download, name="certificate_download"),
]
