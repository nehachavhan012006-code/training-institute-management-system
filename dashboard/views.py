from django.shortcuts import render

from students.models import Student
from trainers.models import Trainer
from courses.models import Course
from exams.models import Exam

def dashboard_home(request):

    context = {
        'total_students': Student.objects.count(),
        'total_trainers': Trainer.objects.count(),
        'total_courses': Course.objects.count(),
        'total_exams': Exam.objects.count(),
    }

    return render(request, 'dashboard/home.html', context)