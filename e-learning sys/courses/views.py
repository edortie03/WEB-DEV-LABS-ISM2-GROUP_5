from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CourseForm, LessonForm
from .models import Course, Enrollment


@login_required
def course_list(request):
    courses = Course.objects.select_related("instructor").all()
    enrolled_ids = set(
        Enrollment.objects.filter(student=request.user).values_list("course_id", flat=True)
    )
    return render(
        request,
        "courses/course_list.html",
        {"courses": courses, "enrolled_ids": enrolled_ids},
    )


@login_required
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    is_enrolled = Enrollment.objects.filter(student=request.user, course=course).exists()
    is_owner = request.user == course.instructor
    lessons = course.lessons.all() if is_enrolled or is_owner else []
    return render(
        request,
        "courses/course_detail.html",
        {"course": course, "lessons": lessons, "is_enrolled": is_enrolled, "is_owner": is_owner},
    )


@login_required
def enroll(request, pk):
    course = get_object_or_404(Course, pk=pk)
    Enrollment.objects.get_or_create(student=request.user, course=course)
    return redirect("courses:course_detail", pk=pk)


@login_required
def instructor_courses(request):
    courses = Course.objects.filter(instructor=request.user)
    return render(request, "courses/instructor_courses.html", {"courses": courses})


@login_required
def course_create(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.instructor = request.user
            course.save()
            return redirect("courses:instructor_courses")
    else:
        form = CourseForm()
    return render(request, "courses/course_form.html", {"form": form})


@login_required
def lesson_create(request, pk):
    course = get_object_or_404(Course, pk=pk, instructor=request.user)
    if request.method == "POST":
        form = LessonForm(request.POST, request.FILES)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.course = course
            lesson.save()
            return redirect("courses:course_detail", pk=course.pk)
    else:
        form = LessonForm()
    return render(request, "courses/lesson_form.html", {"form": form, "course": course})
