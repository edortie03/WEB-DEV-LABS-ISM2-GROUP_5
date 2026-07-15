from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import RegistrationForm


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("users:dashboard")
    else:
        form = RegistrationForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def dashboard(request):
    if request.user.is_instructor():
        return redirect("courses:instructor_courses")
    return redirect("courses:course_list")
