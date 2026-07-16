from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from xhtml2pdf import pisa

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


@login_required
def certificate_download(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)
    certificate = get_object_or_404(Certificate, student=request.user, course=course)

    html = render_to_string(
        "progress/certificate_pdf.html",
        {
            "site_name": "E-Learning Academy",
            "student_name": request.user.get_full_name() or request.user.username,
            "instructor_name": course.instructor.get_full_name() or course.instructor.username,
            "course": course,
            "issued_at": certificate.issued_at,
        },
    )

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = (
        f'attachment; filename="certificate-{course.pk}-{request.user.pk}.pdf"'
    )
    pisa.CreatePDF(html, dest=response)
    return response
