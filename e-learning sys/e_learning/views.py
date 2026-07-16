from django.shortcuts import redirect, render


def landing(request):
    if request.user.is_authenticated:
        return redirect("users:dashboard")
    return render(request, "landing.html")
