from django.contrib import admin

from .models import Certificate, LessonCompletion


@admin.register(LessonCompletion)
class LessonCompletionAdmin(admin.ModelAdmin):
    list_display = ("student", "lesson", "completed_at")


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "issued_at")
