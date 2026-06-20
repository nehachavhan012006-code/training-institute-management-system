from django.shortcuts import render, redirect, get_object_or_404

from .models import Exam
from .forms import ExamForm


def exam_list(request):

    exams = Exam.objects.all()

    return render(
        request,
        'exams/exam_list.html',
        {'exams': exams}
    )


def add_exam(request):

    if request.method == 'POST':

        form = ExamForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/exams/')

    else:
        form = ExamForm()

    return render(
        request,
        'exams/add_exam.html',
        {'form': form}
    )


def edit_exam(request, id):

    exam = get_object_or_404(
        Exam,
        id=id
    )

    if request.method == 'POST':

        form = ExamForm(
            request.POST,
            instance=exam
        )

        if form.is_valid():
            form.save()
            return redirect('/exams/')

    else:
        form = ExamForm(instance=exam)

    return render(
        request,
        'exams/edit_exam.html',
        {'form': form}
    )


def delete_exam(request, id):

    exam = get_object_or_404(
        Exam,
        id=id
    )

    exam.delete()

    return redirect('/exams/')

def result_list(request):

    exams = Exam.objects.all()

    results = []

    for exam in exams:

        marks = exam.marks

        if marks >= 90:
            grade = "A+"
            result = "PASS"

        elif marks >= 80:
            grade = "A"
            result = "PASS"

        elif marks >= 70:
            grade = "B"
            result = "PASS"

        elif marks >= 60:
            grade = "C"
            result = "PASS"

        elif marks >= 40:
            grade = "D"
            result = "PASS"

        else:
            grade = "F"
            result = "FAIL"

        results.append({
            'student': exam.student,
            'course': exam.course,
            'marks': marks,
            'grade': grade,
            'result': result
        })

    return render(
        request,
        'exams/result_list.html',
        {'results': results}
    )