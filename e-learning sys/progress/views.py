from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from courses.models import Course, Lesson

from .models import Certificate, LessonCompletion


@login_required
def mark_complete(request, lesson_pk):
    lesson = get_object_or_404(Lesson, pk=lesson_pk)
    LessonCompletion.objects.get_or_create(student=request.user, lesson=lesson)
    return redirect("progress:course_progress", course_pk=lesson.course.pk)


@login_required
def course_progress(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)
    lessons = course.lessons.all()
    completed_ids = set(
        LessonCompletion.objects.filter(
            student=request.user, lesson__course=course
        ).values_list("lesson_id", flat=True)
    )
    total = lessons.count()
    done = len(completed_ids)
    percent = int((done / total) * 100) if total else 0

    certificate = None
    if total and done == total:
        certificate, _ = Certificate.objects.get_or_create(student=request.user, course=course)

    return render(
        request,
        "progress/course_progress.html",
        {
            "course": course,
            "lessons": lessons,
            "completed_ids": completed_ids,
            "percent": percent,
            "certificate": certificate,
        },
    )
