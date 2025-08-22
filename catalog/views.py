# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Course

def course_list(request):
    courses = Course.objects.all()
    return render(request, "catalog/course_list.html", {"courses": courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, "catalog/course_detail.html", {"course": course})
