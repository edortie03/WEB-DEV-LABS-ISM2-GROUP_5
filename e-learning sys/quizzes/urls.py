from django.urls import path

from . import views

app_name = "quizzes"

urlpatterns = [
    path("course/<int:course_pk>/", views.quiz_list, name="quiz_list"),
    path("course/<int:course_pk>/create/", views.quiz_create, name="quiz_create"),
    path("<int:pk>/take/", views.take_quiz, name="take_quiz"),
    path("result/<int:pk>/", views.quiz_result, name="quiz_result"),
]
