from django.urls import path
from . import views

urlpatterns = [
    path('pgs/', views.progress_index)
]