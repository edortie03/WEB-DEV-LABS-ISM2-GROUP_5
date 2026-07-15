from django import forms

from e_learning.forms import BootstrapFormMixin

from .models import Course, Lesson


class CourseForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Course
        fields = ["title", "description"]


class LessonForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ["title", "content", "pdf", "order"]
        labels = {"content": "Course content"}
