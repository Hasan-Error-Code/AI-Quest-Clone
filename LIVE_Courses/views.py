from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'LIVE_Courses/live_course.html')