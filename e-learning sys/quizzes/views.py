from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from courses.models import Course

from .models import Quiz, QuizResult


@login_required
def quiz_list(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)
    quizzes = course.quizzes.all()
    return render(request, "quizzes/quiz_list.html", {"course": course, "quizzes": quizzes})


@login_required
def take_quiz(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    questions = quiz.questions.prefetch_related("choices").all()

    if request.method == "POST":
        score = 0
        for question in questions:
            selected = request.POST.get(f"question_{question.id}")
            if selected and question.choices.filter(id=selected, is_correct=True).exists():
                score += 1
        result = QuizResult.objects.create(
            student=request.user, quiz=quiz, score=score, total=questions.count()
        )
        return redirect("quizzes:quiz_result", pk=result.pk)

    return render(request, "quizzes/take_quiz.html", {"quiz": quiz, "questions": questions})


@login_required
def quiz_result(request, pk):
    result = get_object_or_404(QuizResult, pk=pk, student=request.user)
    return render(request, "quizzes/quiz_result.html", {"result": result})


@login_required
def quiz_create(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk, instructor=request.user)
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Quiz.objects.create(course=course, title=title)
            return redirect("courses:course_detail", pk=course.pk)
    return render(request, "quizzes/quiz_form.html", {"course": course})
