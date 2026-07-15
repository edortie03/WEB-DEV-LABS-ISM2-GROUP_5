from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = "student", "Student"
        INSTRUCTOR = "instructor", "Instructor"

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.STUDENT)

    def is_student(self):
        return self.role == self.Role.STUDENT

    def is_instructor(self):
        return self.role == self.Role.INSTRUCTOR
